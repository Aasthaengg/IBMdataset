from collections import defaultdict

N = int(input())
S = input()
d = defaultdict(int)
for char in S:
    d[char] += 1

temp = 1
for key in d:
    # print(key, d[key])
    temp *= d[key] + 1
    temp %= 10**9 + 7

ans = temp - 1
print(ans)
