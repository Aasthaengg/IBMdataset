"""
区間ごとに前処理しておけばよい
"""
#memo[i][j] => iから出発し、jまでのどこかで終点する電車の数
N,M,Q = map(int,input().split())
memo = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    l,r = map(int,input().split())
    for j in range(r,N+1):
        memo[l][j] += 1

for _ in range(Q):
    p,q = map(int,input().split())
    ans = 0
    for i in range(p,q+1):
        ans += memo[i][q]
    print(ans)