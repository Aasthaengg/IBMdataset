N,X=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
b=0
for i in range(0,N):
    if X>=a[i]:
        X=X-a[i]
        b+=1
        if i==len(a)-1 and (X+a[i])!=a[i]:
            b-=1
            break
    else:
        break
print(b)