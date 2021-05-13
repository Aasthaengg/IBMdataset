r,g,b,n=map(int,input().split())
p=0
i,j=0,0
while j < n+1:
    k=i*r+j*g
    if (n-k)%b==0 and k <= n:
        #print(i,j,n-k)
        p+=1
    i+=1
    if i>n:
        i=0
        j+=1
print(p)
