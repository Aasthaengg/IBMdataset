MOD = 10**9+7
n = int(input())
s1 = input()
s2 = input()
res = 1
skip = False
for i in range(n):
    if skip:
        skip = False
        continue
    if i == 0:
        if s1[i] != s2[i]:
            res *= 3 * 2
            skip = True
        else:
            res *= 3
        res %= MOD
    else:
        if s1[i] != s2[i]:
            if s1[i-1] != s2[i-1]:
                res *= 3
            else:
                res *= 2
            skip = True
        else:
            if s1[i-1] != s2[i-1]:
                pass
            else:
                res *= 2
        res %= MOD
print(res)