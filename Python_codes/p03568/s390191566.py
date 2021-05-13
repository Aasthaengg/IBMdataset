n = int(input())
a = list(map(int,input().split()))

b = [[] for _ in range(n)]
for i in range(n):
    b[i] = [i for i in range(max(0,a[i]-1),a[i]+2)]


def dfs(i,v,n,b):
    if i==n:
        if v==0:
            return 1
        else:
            return 0
    else:
        res = 0
        for j in b[i]:
            res += dfs(i+1,v*(j%2),n,b)

        return res
    

ans = dfs(0,1,n,b)
print(ans)