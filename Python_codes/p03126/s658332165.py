n,m=map(int,input().split())
ka= [list(map(int,input().split())) for i in range(n)]
for i in range(n):
    ka[i].pop(0)
ans = ka[0]
for i in range(1,n):
    ans = set(ans) & set(ka[i])
print(len(ans))