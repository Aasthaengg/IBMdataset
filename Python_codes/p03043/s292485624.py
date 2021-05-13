A=list(map(int,input().split()))
N=A[0]
K=A[1]
p=0
for i in range(1,N+1):
    count=0
    while i<=K-1:
        i=i*2
        count=count+1
    p=p+(1/2)**(count)
print(p/N)