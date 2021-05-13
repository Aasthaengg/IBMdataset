import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]
dij=[(1,0),(0,1),(-1,0),(0,-1)]

def dfs(i,j):
    cnt=[0]*2
    color=ss[i][j]
    ss[i][j]=2
    cnt[color]+=1
    for di,dj in dij:
        ni,nj=i+di,j+dj
        if ni<0 or ni>=h or nj<0 or nj>=w:continue
        if ss[ni][nj]!=1-color:continue
        ret=dfs(ni,nj)
        cnt[0]+=ret[0]
        cnt[1] += ret[1]
    return cnt

h,w=MI()
ss=[[c=="#" for c in SI()] for _ in range(h)]
ans=0
for i in range(h):
    for j in range(w):
        if ss[i][j]==2:continue
        black,white=dfs(i,j)
        #print(i,j,black,white)
        ans+=black*white
print(ans)
