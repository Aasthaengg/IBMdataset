import math

A,B=map(int,input().split())

C=sorted([A,B])
n=100
h=n
w=n


List=[None]*n
for i in range(n):
    List[i]=[0]*n
 
Col=n//4-1

for i in range(C[1]):
    hh=i//(Col)
    ww=i-hh*(Col)

    if ww%2==0:
         List[(hh+1)*4-1][ww*4]=1
         List[(hh+1)*4-1][ww*4+1]=1
         List[(hh+1)*4-1][ww*4+2]=1
         List[(hh+1)*4-1][ww*4+3]=1


    if ww%2==1:
        List[(hh+1)*4][ww*4]=1
        List[(hh+1)*4][ww*4+1]=1
        List[(hh+1)*4][ww*4+2]=1
        List[(hh+1)*4][ww*4+3]=1

            


for i in range(C[0]-1):
    hh=i//(Col)
    ww=i-hh*(Col)
    if hh==0:
        if ww%2==0:
            List[(hh+1)*4-2][ww*4+2]=1
            List[(hh+1)*4-3][ww*4+2]=1
            List[(hh+1)*4-4][ww*4+2]=1
        if ww%2==1:
            List[(hh+1)*4-1][ww*4+2]=1
            List[(hh+1)*4-2][ww*4+2]=1
            List[(hh+1)*4-3][ww*4+2]=1
            List[(hh+1)*4-4][ww*4+2]=1
    
    else:
        if ww%2==0:
            List[(hh+1)*4-2][ww*4+2]=1
            List[(hh+1)*4-3][ww*4+2]=1
            List[(hh+1)*4-4][ww*4+1]=1

        if ww%2==1:
            List[(hh+1)*4-1][ww*4+2]=1
            List[(hh+1)*4-2][ww*4+2]=1
            List[(hh+1)*4-3][ww*4+1]=1

print(h,w)

if A<=B:
    for i in range(n):
        for j in range(n):
            if List[i][j]==0:
                print(".",end="")
            else:
                print("#",end="")

        if i!=n:
            print("")

else:
    for i in range(n):
        for j in range(n):
            if List[i][j]==0:
                print("#",end="")
            else:
                print(".",end="")

        if i!=n:
            print("")


        
