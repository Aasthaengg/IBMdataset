import math
N,K = map(int, input().split())
ans = 0
for n in range(1, N + 1):
    cnt = 0
    sums = n
    while sums < K:
        sums *= 2
        cnt += 1
    ans += 0.5 ** cnt
print(ans/N)