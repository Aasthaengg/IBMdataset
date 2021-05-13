def check(s,e,t):
    global ans
    if(not s or not e or not t):
        return
    ans=min(ans,(len(s)-1)*10+abs(A-sum(s))+(len(e)-1)*10+abs(B-sum(e))+(len(t)-1)*10+abs(C-sum(t)))

def dfs(s,e,t,i):
    if(i==N):
        check(s,e,t)
        return
    dfs(s,e,t,i+1)
    dfs(s+[l[i]],e,t,i+1)
    dfs(s,e+[l[i]],t,i+1)
    dfs(s,e,t+[l[i]],i+1)

N,A,B,C=map(int,input().split())
l=[int(input()) for i in range(N)]

ans=10**18
dfs([],[],[],0)
print(ans)