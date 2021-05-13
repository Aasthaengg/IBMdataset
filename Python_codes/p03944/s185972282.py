w,h,n = map(int,input().split())
A = [list(map(int,input().split())) for i in range(n)]
sx,sy=0,0
for j in range(n):
    
    if A[j][2]==1 and sx<A[j][0]:
        sx=A[j][0]

    if A[j][2]==2 and w>A[j][0]:
        w=A[j][0]

    if A[j][2]==3 and sy<A[j][1]:
        sy=A[j][1]

    if A[j][2]==4 and h>A[j][1]:
        h=A[j][1]

if (w-sx)<0 or (h-sy)<0 :
    print(0)
else:
    print((w-sx)*(h-sy))