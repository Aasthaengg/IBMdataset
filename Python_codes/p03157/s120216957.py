from collections import deque
H,W=map(int,input().split())
S=["*"*(W+2) for _ in range(H+2)]
for i in range(1,H+1):
    S[i]="*"+input()+"*"

K=0
T=[[0]*(W+2) for _ in range(H+2)]
Neighborhood=[(0,1),(0,-1),(1,0),(-1,0)]
p=0

for y in range(1,H+1):
    for x in range(1,W+1):
        if T[y][x]==0:
            p+=1

            if S[y][x]=="#":
                Black,White=1,0
            elif S[y][x]==".":
                Black,White=0,1

            Q=deque([(x,y)])
            T[y][x]=p

            while Q:
                (u,v)=Q.popleft()
                for (a,b) in Neighborhood:
                    if S[v][u]=="#" and S[v+b][u+a]=="." and T[v+b][u+a]==0:
                        Q.append((u+a,v+b))
                        White+=1
                        T[v+b][u+a]=p
                    elif S[v][u]=="." and S[v+b][u+a]=="#" and T[v+b][u+a]==0:
                        Q.append((u+a,v+b))
                        Black+=1
                        T[v+b][u+a]=p

            K+=Black*White
print(K)