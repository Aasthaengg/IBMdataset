import sys

N = int(input())
A = list(map(int, sys.stdin.readline().rsplit()))
B = list(map(int, sys.stdin.readline().rsplit()))
C = [0] * N

s = 0
minus = 0
res = 0
for i in range(N):
    c = A[i] - B[i]
    C[i] = c
    s += c
    if c < 0:
        minus += c
        res += 1

if s < 0:
    print(-1)
else:
    C.sort(reverse=True)
    s = 0
    for i, c in enumerate(C):
        if s + minus >= 0:
            print(res + i)
            exit()
        s += c
