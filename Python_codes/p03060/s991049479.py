def dfs(now,val,cost):
    if now == n:
        return val - cost
    else:
        return max(dfs(now+1,val+v[now],cost+c[now]),dfs(now+1,val,cost))

n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))

print(dfs(0,0,0))
