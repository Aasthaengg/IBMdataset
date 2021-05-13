n,A,B,C=map(int,input().split())

l=[int(input()) for _ in range(n)]



def dfs(count,a,b,c):
    if count==n:
        if min(a,b,c)>0:
            return abs(a-A)+abs(b-B)+abs(c-C)-30
        else:
            return 10**9+1
    x = dfs(count+1, a, b, c)
    y = dfs(count+1, a+l[count], b, c)+10
    z = dfs(count+1, a, b+l[count], c)+10
    w = dfs(count+1, a, b, c+l[count])+10
    return min(x,y,z,w)



print(dfs(0,0,0,0))