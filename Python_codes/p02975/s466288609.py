N=int(input())
A=list(map(int,input().split()))

T={}
for a in A:
    if a in T:
        T[a]+=1
    else:
        T[a]=1

F=True
for x in T:
    F&=(3*T[x]%N==0)

if not F:
    print("No")
    exit()

M=max(T,key=lambda x:T[x])
if 3*T[M]==N:
    x,y,z=list(T.keys())
elif 3*T[M]==2*N:
    x=y=M
    del T[M]
    z=tuple(T.keys())[0]
else:
    x=y=z=M

if x^y==z:
    print("Yes")
else:
    print("No")

