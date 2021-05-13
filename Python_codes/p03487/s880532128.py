from collections import defaultdict

n = int(input())
a_list = [int(x) for x in input().split()]

d = defaultdict(int)
for a in a_list:
    d[a] += 1

ans = 0
for i, c in d.items():
    ans += c - i if c >= i else c
print(ans)