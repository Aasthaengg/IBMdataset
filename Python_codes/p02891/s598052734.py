from itertools import groupby

s = input()
k = int(input())

cont = [sum(1 for _ in it) for k, it in groupby(s)]

if len(cont) == 1:
    res = len(s) * k // 2
else:
    res = k-1 if s[0] == s[-1] and cont[0] % 2 == 1 and cont[-1] % 2 == 1 else 0
    for c in cont:
        if c != 1:
            res += c // 2 * k

print(res)
