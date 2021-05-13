import sys

stdin = sys.stdin
 
ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N = ri()
A = rl()
answer = 0
for i in range(N):
    if A[A[i]-1]-1 == i:
        answer += 1

print(answer//2)
