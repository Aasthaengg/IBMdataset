import sys
from collections import deque
def tsort(n,g,inc):
    s,tsl=deque(),[]
    s.extend([i for i,x in enumerate(inc) if x==0])
    while len(s)>0:
        x=s.popleft()
        tsl.append(x)
        for y in g[x]:
            inc[y]-=1
            if inc[y]==0:s.append(y)
    return tsl
def main():
    N,M=tuple(map(int,sys.stdin.readline().split()))
    lpl,inc,g=[0 for _ in range(N)],[0 for _ in range(N)],[[] for _ in range(N)]
    for _ in [0]*M:
        x,y=tuple(map(int,sys.stdin.readline().split()))
        inc[y-1]+=1
        g[x-1].append(y-1)
    tsl=tsort(N,g,inc)
    for t in tsl:
        for n in g[t]:lpl[n]=lpl[t]+1 if lpl[t]+1>lpl[n] else lpl[n]
    print(max(lpl))
if __name__=='__main__':main()