N=int(input())
A=list(map(int,input().split()))


ABS=[abs(A[i]) for i in range(N)]

x=max(ABS)
ki=ABS.index(x)

ANSLIST=[]
for i in range(ki):
    ANSLIST.append((ki+1,i+1))

for j in range(ki+1,N):
    ANSLIST.append((ki+1,j+1))

if A[ki]>0:
    for i in range(N-1):
        ANSLIST.append((i+1,i+2))
elif A[ki]<0:
    for i in range(N-1,0,-1):
        ANSLIST.append((i+1,i))

print(len(ANSLIST))

for ans in ANSLIST:
    print(ans[0],ans[1])

