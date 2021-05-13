N = int(input())
out=0
k=0
for i in range(1,N+1):
    k=0
    if i % 2==1:
        for j in range(1,i+1):
            if i % j==0:
                k = k+1
        if k==8:
            out = out+1
    
print(out) 