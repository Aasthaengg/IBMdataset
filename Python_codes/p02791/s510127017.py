import sys

N = int(sys.stdin.readline().rstrip())
P = [int(x) for x in sys.stdin.readline().rstrip().split()]

m = N  # iの前までの最小
cnt = 0
for i in range(N):
    if m >= P[i]:
        cnt += 1
    m = min(m,P[i])

print(cnt)