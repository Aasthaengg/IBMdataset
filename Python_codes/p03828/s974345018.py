n=int(input())
ans=1
rec=[True]*(n+1)
for i in range(2,n+1):
    if rec[i]:
        x=1
        for j in range(1,n+1):
            y=j
            if y%i==0:
                rec[y]=False
            while y%i==0:
                x+=1
                y=y//i
        ans=(ans*x)%1000000007
print(ans)