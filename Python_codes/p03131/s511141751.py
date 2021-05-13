K,A,B=map(int,input().split())
if A+2>=B:
    print(K+1)
elif K<=A:
    print(K+1)
else:
    K-=A-1
    k=K//2
    print(B*k-A*(k-1)+K%2)