import sys
sys.setrecursionlimit(4100000)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
g = [[]*(n*(n-1)//2) for _ in range(n*(n-1)//2)]
chk = set([])
cnt = 0
d = {}
st = set([])

for i in range(n):
  a = [int(i) for i in readline().split()]
  for j in range(n-2):
    A,b = min(a[j],i+1),max(a[j],i+1)
    p,q = min(a[j+1],i+1),max(a[j+1],i+1)    
    if not b*1000+A in chk:
      d[b*1000+A] = cnt
      cnt += 1
      chk.add(b*1000+A)
    if not q*1000+p in chk:
      d[q*1000+p] = cnt
      cnt += 1
      chk.add(q*1000+p)
    g[d[b*1000+A]].append(d[q*1000+p])
    if j == 0:
      st.add(d[b*1000+A])

# あとは頂点VのグラフをdfsしてLongest pathの長さを求める
# -1: unchecked, -2: checked and uncalculated
dp=[-1]*(n*(n-1)//2)
#flag=True
def dfs(v):
    #global flag
    dp[v]=-2
    length=0
    for nv in g[v]:
        if(dp[nv]==-2):
            print(-1)
            exit()
        if(dp[nv]==-1):
            dfs(nv)
        length=max(length,dp[nv]+1)
    dp[v]=length
            
st = list(st)
a = []
pp = 0
for i in st:dfs(i)
print(max(dp)+1)
