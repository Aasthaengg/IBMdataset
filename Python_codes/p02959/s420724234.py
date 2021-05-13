import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

sum = 0
for i in range(N):
    d1 = min(A[i], B[i])
    A[i] -= d1
    B[i] -= d1
    sum += d1
    d2 = min(A[i+1], B[i])
    A[i+1] -= d2
    B[i] -= d2
    sum += d2

print(sum)

