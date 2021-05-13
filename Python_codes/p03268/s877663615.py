n,k=map(int,input().split())
ans=0
for i in range(1,n+1):
    c=0
    if 2*i%k==0:
        c+=1+(n+i)//k+(-1-i)//k
    #python3 a.pyprint(c)
    ans+=c**2
print(ans)