import sys

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N, T = rl()
A = rl()
answer = 1
profit = 0
min = A[0]
for i in range(1, N):
    if A[i] < min:
        min = A[i]
        continue
    x = A[i] - min
    if x > profit:
        answer = 1
        profit = x
    elif x == profit:
        answer += 1

print(answer)
# 40
