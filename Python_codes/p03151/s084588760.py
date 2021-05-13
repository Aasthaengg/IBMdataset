N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
P = sorted([A[i]-B[i] for i in range(N) if A[i]-B[i]>0],reverse=True)
C = [0 for _ in range(N+1)]
for i in range(1,len(P)+1):
    C[i] = C[i-1]+P[i-1]
M = [B[i]-A[i] for i in range(N) if B[i]-A[i]>0]
p = sum(P)
m = sum(M)
if m>p:
    ans = -1
else:
    if len(M)==0:
        ans = 0
    else:
        for i in range(1,len(P)+1):
            if C[i]>=m:
                ans = i
                break
        ans += len(M)
print(ans)