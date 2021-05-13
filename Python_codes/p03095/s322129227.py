from collections import defaultdict

N = int(input())
S = input()

M = 10**9 + 7
count_dict = defaultdict(int)

for s in S:
    count_dict[s] += 1

ans = 1
for v in count_dict.values():
    ans *= (v + 1)
    ans %= M

print(ans - 1)