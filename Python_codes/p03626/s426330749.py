n = int(input())
s1 = str(input())
s2 = str(input())

L = []

for i in range(n):
    if s1[i] == s2[i]:
        L.append(0)
    else:
        if i == n-1:
            continue
        if s1[i] == s1[i+1]:
            L.append(1)

m = len(L)
ans = 1
mod = 10**9+7
for i in range(m):
    if i == 0:
        if L[i] == 0:
            ans *= 3
        else:
            ans *= 6
        ans %= mod
    else:
        if L[i-1] == 0 and L[i]== 0:
            ans *= 2
        elif L[i-1] == 0 and L[i] == 1:
            ans *= 2
        elif L[i-1] == 1 and L[i] == 0:
            ans *= 1
        else:
            ans *= 3
        ans %= mod
ans %= mod
print(ans)