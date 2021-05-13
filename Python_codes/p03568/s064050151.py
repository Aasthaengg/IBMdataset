import sys

def dfs(x,m,nex):
    if m==n:
        #print(x)
        if x%2==0:
            global ans
            ans += 1
    else:
        ai = a[nex]
        m += 1
        nex += 1
        for i in (ai,ai-1,ai+1):
            dfs(x*i,m,nex)

sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in (a[0],a[0]-1,a[0]+1):
    dfs(i,1,1)
print(ans)