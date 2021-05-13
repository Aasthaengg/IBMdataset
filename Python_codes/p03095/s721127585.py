from collections import Counter

N = int(input())
S = input()

d = Counter(S)

m = 10 ** 9 + 7
# print(d)
ans = 1
for k, v in d.items():
    ans = ans * (v + 1) % m
print((ans - 1) % m)

