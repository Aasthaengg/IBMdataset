n = int(input())
s1 = input()
s2 = input()
mod = 10**9 + 7

if s1[0] == s2[0]:
    ans = 3
    q = 1
else:
    ans = 6
    q = -1

for i in range(1, n):
    x = s1[i]
    y = s2[i]
    if x == y:
        if q == 0:
            q = 1
        elif q == 1:
            ans *= 2
    else:
        if q == -1:
            q = 0
        elif q == 0:
            ans *= 3
            q = -1
        else:
            ans *= 2
            q = -1
    ans %= mod
print(ans%mod)
