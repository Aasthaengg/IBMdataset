import sys
sys.setrecursionlimit(2147483647)
 
h,w=map(int,input().split())
s=list(input() for _ in range(h))
 
yoko=[[0]*w for _ in range(h)]
tate=[[0]*w for _ in range(h)]
 
def yoko_check(y,x,cnt):
    global yoko,s
    if x==w-1:
        yoko[y][x]=cnt
        return cnt
    else:
        if s[y][x+1]=="#":
            yoko[y][x]=cnt
            return cnt
        else:
            yoko[y][x]=yoko_check(y,x+1,cnt+1)
            return yoko[y][x]
 
 
def tate_check(y,x,cnt):
    global tate,s
    if y==h-1:
        tate[y][x]=cnt
        return cnt
    else:
        if s[y+1][x]=="#":
            tate[y][x]=cnt
            return cnt
        else:
            tate[y][x]=tate_check(y+1,x,cnt+1)
            return tate[y][x]
 
 
for y in range(h):
    for x in range(w):
        if yoko[y][x]==0 and s[y][x]==".":
            yoko_check(y,x,1)
        if tate[y][x]==0 and s[y][x]==".":
            tate_check(y,x,1)
 
#print(tate)
 
result=0
for y in range(h):
    for x in range(w):
        if s[y][x]==".":
            result=max(result,tate[y][x]+yoko[y][x]-1)  
 
print(result)  