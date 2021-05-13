N = int(input())

A = [None for _ in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split()))

#ワーシャルフロイド法で条件を満たすものがあるか確認
for k in range(N):
    for i in range(N):
        for j in range(N):
            if A[i][j] > A[i][k] + A[k][j]:
                print(-1)
                exit()

ans = 0
for i in range(N-1):
    for j in range(i,N):
        for k in range(N):
            if i == k or j == k:
                continue
            if A[i][j] == A[i][k] + A[k][j]: # A[i][j]はiとjのノードを直接結ぶものではない
                break
        else:
            ans += A[i][j]

print(ans) 