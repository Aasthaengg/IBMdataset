s = list(str(input()))
k = int(input())

n = len(s)

cur = s[0]
L = []
cnt = 0
for i in range(n):
    if cur == s[i]:
        cnt += 1
    else:
        L.append(cnt)
        cur = s[i]
        cnt = 1
else:
    L.append(cnt)
#print(L)

if s[0] != s[-1]:
    C = 0
    for i in range(len(L)):
        if L[i] >= 2:
            C += L[i]//2
    ans = C*k
else:
    if len(L) >= 2:
        C = 0
        for i in range(1, len(L)-1):
            if L[i] >= 2:
                C += L[i]//2
        ans = C*k
        ans += L[0]//2+L[-1]//2+((L[0]+L[-1])//2)*(k-1)
    else:
        ans = (L[0]*k)//2
print(ans)
