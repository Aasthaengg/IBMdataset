import sys

N = int(input())
A = list(map(int, sys.stdin.readline().rsplit()))
B = list(map(int, sys.stdin.readline().rsplit()))

a = 0
b = 0
for i in range(N):
    if A[i] > B[i]:
        a += A[i] - B[i]
    elif B[i] > A[i]:
        b += (B[i] - A[i]) // 2

if b >= a:
    print("Yes")
else:
    print("No")
