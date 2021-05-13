import sys
sys.setrecursionlimit(10**9)

def f(x):#dpは
    if dp[x]!=-1:
        return dp[x]#すでに値が決まっていたらそれをかえす
    ans=0
    for e in d[x]:#すべての枝について
        ans=max(ans,1+f(e))
    dp[x]=ans
    return ans

n,m = list(map(int, input().split()))

d={}
dp=[-1]
for i in range(1,n+1):
    d[i]=[]#dは初期値を[]
    dp.append(-1)#dpは初期値-1

for _ in range(m):
    a,b = map(int, input().split())
    d[a].append(b)#有向グラフをdictで
    
ans=0
for i in range(1,n+1):
    ans=max(ans,f(i))
print(ans)