n = int(input())
s1 = input()
s2 = input()
mod = 10**9+7
def tate(i, s1, s2):
    return s1[i] == s2[i]

ans = 1
for i in range(n-1):
    if s1[i] == s1[i+1]:
        continue
    cur_tate = tate(i, s1, s2)
    nex_tate = tate(i+1, s1, s2)
    if cur_tate and nex_tate:
        ans *= 2
    elif cur_tate and not nex_tate:
        ans *= 2
    elif not cur_tate and not nex_tate:
        ans *= 3
    else:
        continue
    ans %= mod

if tate(0, s1, s2):
    print(3*ans%mod)
else:
    print(6*ans%mod)
