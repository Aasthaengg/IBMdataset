import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000000)
MOD = 10**9+7

n,k=map(int,input().split())
tree=[[] for _ in range(n)]

for _ in range(n-1):
        a,b=map(int,input().split())
        a-=1
        b-=1
        tree[a].append(b)
        tree[b].append(a)

ans=k   
def dfs(i,before=-1):
    global ans 

    if i==0:
        j=1
    else:
        j=2
        
    for e in tree[i]:
        if e!=before:
            ans*=(k-j)
            ans%=MOD
            j+=1
            dfs(e,i)
dfs(0)
print(ans)  