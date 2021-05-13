S = list(input())

Wcnt = 0
res = 0

for i in range(len(S)):
    if S[i] == 'W':
        res += i - Wcnt
        Wcnt += 1

print(res)