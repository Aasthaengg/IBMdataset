from collections import deque
H,W=map(int,input().split())
S=[]
count=0
for _ in range (H):
    A=list(input())
    for a in A:
        if a=='.':
            count+=1
    S.append(A)
 
mas=deque([(0,0,0)])
while mas:
    y,x,n=mas.popleft()
    if 0<=y<=H-1 and 0<=x<=W-1:
        if S[y][x]=='.':
            S[y][x]=n
            mas.append((y+1,x,n+1))
            mas.append((y,x+1,n+1))
            mas.append((y-1,x,n+1))
            mas.append((y,x-1,n+1))
short=S[H-1][W-1]
if short=='.':
    print(-1)
else:
    print(count-(short+1))