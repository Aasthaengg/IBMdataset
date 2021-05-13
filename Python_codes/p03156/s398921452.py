N=int(input())
A,B=map(int,input().split())
*P,=map(int,input().split())

X=Y=Z=0
for p in P:
    if p<=A:
        X+=1
    elif B<p:
        Z+=1
    else:
        Y+=1

print(min([X,Y,Z]))