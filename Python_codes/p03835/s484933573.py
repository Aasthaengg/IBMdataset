import itertools
K, S = map(int, input().split())
ans = 0

for i in itertools.product(range(K+1), repeat=2):
    if 0 <= (S - sum(i)) <= K:
        ans += 1
print(ans)