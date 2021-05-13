N,a,b = map(int, input().split())
sum=0
for i in range(1,N+1):
    c=0
    d=i
    while d>0:
        c+=d%10
        d//=10
    if a<=c<=b:
        sum+=i
    
print(sum)