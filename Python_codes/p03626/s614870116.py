mod = 10**9+7
N = int(input())
s1 = input()
s2 = input()
ans = 1
cur = 0
i = 0
while i < N:
    if s1[i] == s2[i]:
        ans *= 3-cur
        ans %= mod
        i += 1
        cur = 1
    else:
        if cur == 2:
            ans *= 3
        else:
            ans *= (3-cur)*(2-cur)
        ans %= mod
        i += 2
        cur = 2
print(ans)