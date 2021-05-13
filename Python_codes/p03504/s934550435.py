import sys
input = sys.stdin.readline
n,c=map(int,input().split())
prog=[]
stc=[]
for i in range(n):
    x=tuple(map(int,input().split()))
    stc.append(x)
stc=sorted(stc)
video=[[0]*(10**5+1) for i in range(30)]
for s,t,ci in stc:
    if video[ci-1][s]!=-1:
        video[ci-1][s-1]+=1
        video[ci-1][t]-=1
    else:
        video[ci-1][s]=0
        video[ci-1][t]-=1
newvideo=[]
for i in range(10**5+1):
    cnt=0
    for c in range(30):
        cnt+=video[c][i]
    newvideo.append(cnt)

from itertools import accumulate
videoacc=list(accumulate(newvideo))

print(max(videoacc))