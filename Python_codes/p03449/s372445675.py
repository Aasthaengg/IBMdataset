from itertools import accumulate


N = int(input())
A1 = [0] + list(accumulate(map(int, input().split())))
A2 = [0] + list(accumulate(map(int, input().split())))
ans = 0
for i in range(1, N + 1):
    cur = A1[i - 1]
    if i < N:
        cur += A2[N] - A2[i]
    ans = max(ans, cur + A1[i] - A1[i - 1] + A2[i] - A2[i - 1])
print(ans)
