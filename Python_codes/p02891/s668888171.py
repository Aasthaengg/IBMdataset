s = str(input())
k = int(input())

n = len(s)

s_ = list(s)
if len(set(s_)) == 1:
    print((n*k)//2)
    exit()

cur = s[0]
X = []
cnt = 0
for i in range(n):
    if s[i] != cur:
        X.append(cnt)
        cur = s[i]
        cnt = 1
    else:
        cnt += 1
else:
    X.append(cnt)

#print(X)
ans = 0
if s[0] != s[-1]:
    for x in X:
        ans += k*(x//2)
else:
    for i, x in enumerate(X):
        if i == 0 or i == len(X)-1:
            continue
        else:
            ans += k*(x//2)
    ans += X[0]//2
    ans += X[-1]//2
    ans += (k-1)*((X[0]+X[-1])//2)
print(ans)
