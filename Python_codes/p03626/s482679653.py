n = int(input())
s0 = input().rstrip()
s1 = input().rstrip()
v = True
index = 0
res = 3
while index < n:
    vv = s0[index] == s1[index]
    if index == 0 and vv:
        pass
    elif v:
        res *= 2
    elif not v and not vv:
        res *= 3
    index += 1 if vv else 2
    v = vv
MOD = 10**9 + 7
print(res % MOD)