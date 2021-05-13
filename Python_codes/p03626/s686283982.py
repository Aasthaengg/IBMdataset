n = int(input())
# s = [list(input()) for _ in range(2)]
s1 = input()
s2 = input()

MOD = 10 ** 9 + 7

i = 0
pattern = 0
res = 1
while i < n:
    if s1[i] == s2[i]:
        i += 1
        res *= (3 - pattern)
        pattern = 1
    else:
        i += 2
        if pattern == 1:
            res *= 2
        elif pattern == 2:
            res *= 3
        else:
            res *= 6
        pattern = 2
    res %= MOD

res %= MOD
print(res)