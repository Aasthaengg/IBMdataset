n=int(input())
res=1
k=1
for b in range(1,int(n**0.5)+1):
    for p in range(2,n):
        if b**p>n:
            break
        else:
            res=max(res,b**p)
print(res)