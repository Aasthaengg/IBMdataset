A,B,C,K=map(int,input().split())
x =K-A
y =x-B
if x<=0:
    print(K)
else:
    if y<=0:
        print(A)
    else:
        print(A-y) 