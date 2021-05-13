MOD=10**9+7
N = int(input())
s1 = list(input())
s2 = list(input())
pre = s1[0] == s2[0]
if s1[0] == s2[0]:
    ans = 3
    idx = 1

else:
    ans = 6
    idx = 2
while idx < N:
    if pre:
        ans *= 2
    else:
        if s1[idx] != s2[idx]:
            ans *= 3

    pre=s1[idx] == s2[idx]
    if s1[idx] == s2[idx]:
        idx += 1
    else:
        idx += 2

print(ans%MOD)
