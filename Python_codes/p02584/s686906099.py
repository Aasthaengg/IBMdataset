xkd = input().split()
X = int(xkd[0])
K = int(xkd[1])
D = int(xkd[2])

X = abs(X)
ans = 0
times = int(X/D)
oneMore = False
if X%D > abs(D-X%D):
    times+=1

if times > K:
    ans = X - (D*K)
else:
    if (times%2) == (K%2):
        ans = min(X%D, (D-X%D))
    else:
        ans = max(X%D, (D-X%D))

print(ans)