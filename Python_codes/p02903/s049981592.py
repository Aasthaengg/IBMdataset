# A - 01 Matrix
H,W,A,B = map(int,input().split())
for i in range(H):
    for j in range(W):
        print((int(i<B)+int(j<A))%2,sep='',end='')
    print('')