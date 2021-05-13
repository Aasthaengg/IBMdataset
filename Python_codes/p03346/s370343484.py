n = int(input())
p = [int(input()) for _i in range(n)]

visit = [-1 for _i in range(n+1)]
for i in p:
    if visit[i-1] < 0:
        visit[i] = 1
    else:
        visit[i] = visit[i-1]+1
print(n-max(visit))