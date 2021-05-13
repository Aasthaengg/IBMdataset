n=int(input())
k=int(input())
xs=list(map(int,input().split(' ')))
sum =0 
for i in range(n):
    d=abs(xs[i]-k)
    if xs[i]<d:
        sum+=xs[i]*2
    else:
        sum+= d*2
print(sum)