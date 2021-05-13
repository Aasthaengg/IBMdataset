from bisect import bisect_right

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort()
B.sort()
C.sort()

Bcnt = [0]*(N+1)
idx = N
for i in range(N-1,-1,-1):
    idx = bisect_right(C,B[i],hi=idx)
    Bcnt[i] = N-idx+Bcnt[i+1]

ans = 0
idx = 0
for i in range(N):
    idx = bisect_right(B,A[i],lo=idx)
    ans += Bcnt[idx]

print(ans)