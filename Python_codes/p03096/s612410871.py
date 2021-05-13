N = int(input())
C = [int(input()) for _ in range(N)]
before = [-1] * (2 * 10**5 + 1)
count = [0] * (N + 1)
count[-1] = 1
mod = 10**9 + 7
for i in range(N):
    count[i] = count[i - 1]
    if 0 <= before[C[i]] < i - 1:
        count[i] += count[before[C[i]]]
        count[i] %= mod
    before[C[i]] = i
print(count[N - 1])
