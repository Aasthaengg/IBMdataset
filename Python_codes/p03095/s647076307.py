from collections import Counter

N = int(input())
S = input()

C = Counter(S)

res = 1
for v in C.values():
    res *= (v + 1)
    res %= 10 ** 9 + 7

print(res - 1)
