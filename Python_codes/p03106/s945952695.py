a,b,k=map(int,input().split())
m=max(a,b)
i=0
while i<k:
    if a%m==0 and b%m==0:
        i+=1
    m-=1
print(m+1)