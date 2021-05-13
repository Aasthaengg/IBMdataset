N,K=map(int,input().split())
total=0
for i in range(1,N+1):
    if i>=K:
        total+=1
    for j in range(20):
        
        if (2**j)*i<K<=(2**(j+1))*i:
            a=j+1
            total+=(1/2)**a
            break

print((1/N)*total)