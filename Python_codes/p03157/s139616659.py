import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline


def DFS(add,next,cnt):
    x,y=add
    for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
        X,Y=x+i,y+j
        if 0<=X<h and 0<=Y<w:
            if S[X][Y]==next and color[X][Y]=="white":
                color[X][Y]=str(cnt)
                DFS([X,Y],"." if next=="#" else "#",cnt)


h,w=map(int,input().split())
S=[list(input()) for _ in range(h)]
cnt=0

color=[["white" for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if S[i][j]=="#" and color[i][j]=="white":
            cnt +=1
            DFS([i,j],".",cnt)

dictionary={str(i+1):[0,0] for i in range(cnt)}
for i in range(h):
    for j in range(w):
        if color[i][j]!="white":
            if S[i][j]==".":dictionary[color[i][j]][0] +=1
            else:dictionary[color[i][j]][1] +=1

ans=0
for v,m in dictionary.values():
    ans +=v*m
print(ans)