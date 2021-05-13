N, M = map(int,input().split())
ans = [0 for i in range(N)]

for i in range(M):
    ab = list(map(int,input().split()))
    ans[ab[0]-1] += 1
    ans[ab[1]-1] += 1

for i in range(N):
    print(ans[i])