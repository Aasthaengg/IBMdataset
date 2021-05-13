from collections import Counter
N = int(input())
S = ["".join(sorted(input())) for _ in range(N)]
S_counter = Counter(S)
ans = 0
for i in S_counter.values():
    if i > 1:
        ans += (i-1)*i/2
print(int(ans))