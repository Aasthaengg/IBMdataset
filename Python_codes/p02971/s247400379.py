import sys
input = sys.stdin.buffer.readline
N = int(input())
A = [int(input()) for _ in range(N)]
B = A[:]
max1 = max(A)
A.remove(max1)
max2 = max(A)

for i in B:
    if i == max1:
        print(max2)
    else:
        print(max1)
