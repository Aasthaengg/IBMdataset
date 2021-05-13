import sys
 
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
 
A_dash = []
for i in range(N):
    A_dash.append(A[i] - (i + 1))
 
A_dash.sort()
ans = -float("inf")
if N % 2 == 1:
    tmp = 0
    b = A_dash[N // 2]
    for i in range(N):
        tmp += abs(A_dash[i] - b)
    print(tmp)
else:
    tmp1 = 0
    b = A_dash[N // 2 - 1]
    for i in range(N):
        tmp1 += abs(A_dash[i] - b)
    
    tmp2 = 0
    b = A_dash[N // 2]
    for i in range(N):
        tmp2 += abs(A_dash[i] - b)
    print(min(tmp1, tmp2))