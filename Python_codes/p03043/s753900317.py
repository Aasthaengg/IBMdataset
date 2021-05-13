n,k=map(int,input().split())
b=0
s=0
for i in range(1,n+1):
    for j in range(20):
        if i*(2**j)>=k:
            s=j
            break
    b+=1/(2**s)
print(b/n)
