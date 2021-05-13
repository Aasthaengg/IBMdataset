# B - Can you solve this?
N,M,C = map(int,input().split())
B = list(map(int,input().split()))
A = [list(map(int,input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    tmp = 0
    for j in range(M):
        tmp += A[i][j]*B[j]
    ans = ans+1 if tmp+C>0 else ans
print(ans)