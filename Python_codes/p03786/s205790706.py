import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int,input().split())))

cnt = 1
for i in range(N-1):
    if A[i]*2 < A[i+1]:
        cnt = 1
    else:
        cnt += 1
    A[i+1] += A[i]

print(cnt)
