a,b,k=map(int,input().split())
turn=1
for i in range(k):
    if turn==1:
        a//=2
        b+=a
    if turn==-1:
        b//=2
        a+=b
    turn*=-1

print(a,b)