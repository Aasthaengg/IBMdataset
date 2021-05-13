N,A,B,C = map(int,(input().split()))
l = [int(input()) for i in range(N)]

def dfs(cur,a,b,c):
    if cur == N:
        if min(a,b,c) > 0:
            return abs(a-A) + abs(b-B) + abs(c-C) -10*3 
        else:
            return 10**9
    c0 = dfs(cur+1,a,b,c)
    c1 = dfs(cur+1,a+l[cur],b,c) +10
    c2 = dfs(cur+1,a,b+l[cur],c) +10
    c3 = dfs(cur+1,a,b,c+l[cur]) +10
    return min(c0,c1,c2,c3)

print(dfs(0,0,0,0))