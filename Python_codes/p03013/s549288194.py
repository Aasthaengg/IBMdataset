# https://atcoder.jp/contests/abc129/tasks/abc129_c

n, m = [int(i) for i in input().split()]
broken = set()
MOD = 10**9 + 7
for _ in range(m):
    broken.add(int(input()))

steps = [0] * (n + 1)
steps[0] = 1
if 1 in broken:
    steps[1] = 0
else:
    steps[1] = 1

for i in range(2, n + 1):
    if i in broken:
        steps[i] = 0
    else:
        steps[i] = (steps[i - 1] + steps[i - 2]) % MOD

print(steps[n])
