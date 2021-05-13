from collections import deque
from bisect import bisect_right
INFTY = 10**6
N,M = map(int,input().split())
S = input().strip()
dp = [INFTY for _ in range(N+1)]
dp[N]=0
A = deque([])
B = {}
pre = N
flag = 0
for i in range(N-1,-1,-1):
    if S[i]=="0":
        ind = bisect_right(A,i+M)
        if ind>0:
            dp[i] = dp[A[ind-1]]+1
            B[i] = A[ind-1]
            if dp[i]>dp[pre]:
                A.appendleft(pre)
        else:
            if pre<=i+M:
                dp[i]=dp[pre]+1
                B[i] = pre
                A.appendleft(pre)
            else:
                flag = 1
                break
        pre = i
if flag==0:
    P = []
    k = 0
    while k<N:
        P.append(B[k]-k)
        k = B[k]
    print(*P)
else:
    print(-1)