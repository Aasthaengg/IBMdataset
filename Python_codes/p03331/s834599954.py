n=int(input())
ans=100000
for a in range(1,n):##正
    b=n-a
    suma=sum(list(map(int, list(str(a)))))
    sumb=sum(list(map(int, list(str(b)))))
    
    ans=min(ans,sumb+suma)
print(ans)