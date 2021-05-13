import sys

N, K = map(int, input().split())
broken = []
for _ in range(K):
    broken.append(int(input()))

for k in range(K-1):
    if broken[k] +1 == broken[k+1]:
        print(0)
        sys.exit(0)
broken_set = set(broken)

# N段連続したら何通りあるか表を作る
P = {0: 1, 1: 1, 2: 2}
for i in range(3, N+1):
    P[i] = P[i-1] + P[i-2]

total = 1
low = 0
for i in range(1, N+1):
    if i in broken_set:
        seq = (i - 1) - low
        total *= P[seq]
        total %= 1000000007
        low = i + 1
else:
    seq = N - low
    total *= P[seq]
    total %= 1000000007

print(total)
