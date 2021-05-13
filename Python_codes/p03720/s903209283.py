N,M = map(int, input().split())
li = [0 for i in range(N)]
for i in range(M):
    x,y = map(int, input().split())
    li[x-1] += 1
    li[y-1] += 1
for i in range(N):
    print(li[i])