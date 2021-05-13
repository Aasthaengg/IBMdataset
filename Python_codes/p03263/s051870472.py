def mover(H,W):
    k=1
    x,y=0,0
    v=1
    while k<H*W:
        old_x,old_y=x,y

        if not((v==1 and x==W-1) or (v==-1 and x==0)):
            x+=v
        else:
            v*=-1
            y+=1
        yield ((old_x,old_y),(x,y))
        k+=1
#------------------------------------------------
H,W=map(int,input().split())
A=[]
for _ in range(H):
    A.append(list(map(int,input().split())))

Mode=0
D=[]
for ((ox,oy),(x,y)) in mover(H,W):
    if (Mode==0 and A[oy][ox]%2==1) or Mode==1:
        A[oy][ox]-=1
        A[y][x]+=1
        D.append(((ox,oy),(x,y)))
        Mode=A[y][x]%2

print(len(D))
for ((ox,oy),(x,y)) in D:
    print(oy+1,ox+1,y+1,x+1)
