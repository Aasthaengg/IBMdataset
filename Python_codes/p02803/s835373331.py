import collections
q=collections.deque()
h,w=map(int,input().split())
S=[]
for _ in range(h):
    s=input()
    S.append(s)
went=[[0]*w for _ in range(h)]
l=[]
def walk(x,y):
    if x<=h-2:
        if S[x+1][y]=='.' and (x+1,y)!=(ih,iw) and went[x+1][y]==0 or went[x+1][y]>went[x][y]+1:
            went[x+1][y]=went[x][y]+1
            q.append((x+1,y))
    if y<=w-2:
        if S[x][y+1]=='.' and (x,y+1)!=(ih,iw) and went[x][y+1]==0 or went[x][y+1]>went[x][y]+1:
            went[x][y+1]=went[x][y]+1
            q.append((x,y+1))
    if y>=1:
        if S[x][y-1]=='.' and (x,y-1)!=(ih,iw) and went[x][y-1]==0 or went[x][y-1]>went[x][y]+1:
            went[x][y-1]=went[x][y]+1
            q.append((x,y-1))
    if x>=1:
        if S[x-1][y]=='.' and (x-1,y)!=(ih,iw) and went[x-1][y]==0 or went[x-1][y]>went[x][y]+1:
            went[x-1][y]=went[x][y]+1
            q.append((x-1,y))
        
for ih in range(h):
    for iw in range(w):
        if S[ih][iw]=='.':
            went=[[0]*w for _ in range(h)]
            q.append((ih,iw))
            while q:
                (a,b)=q.pop()
                walk(a,b)
            
            ll=[]
            for i in range(h):
                ll.append(max(went[i]))
            l.append(max(ll))
            
print(max(l))