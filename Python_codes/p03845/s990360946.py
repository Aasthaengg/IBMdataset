N=int(input())
*T,=map(int,input().split())
M=int(input())
PX=[list(map(int,input().split()))for i in range(M)]

for p,x in PX:
    A=T[p-1]
    T[p-1]=x
    print(sum(T))
    T[p-1]=A