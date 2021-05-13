import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int,input().split())
P = list(map(int,input().split()))

A = [0,0,0]
for i in range(n):
    if P[i] <= a:
        A[0] += 1
    elif P[i] <= b:
        A[1] += 1
    else:
        A[2] += 1
print(min(A))