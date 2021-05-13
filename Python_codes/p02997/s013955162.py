import itertools

N,K=map(int,input().split())

m2=(N-1)*(N-2)//2 - K

if m2>=0:
    M=N-1+m2
    print(M)
    for i in range(1,N):
        print(1,i+1)
    i=0
    for a,b in  itertools.combinations(range(1,N), 2):
        if i==m2:
            break
        print(a+1,b+1)
        i+=1
        
else:
    print(-1)