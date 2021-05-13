n,a,b=map(int,input().split())
x=list(map(int,input().split()))

sum=0
for i in range(n-1):
    A=(x[i+1]-x[i])*a
    if A>b:
        sum += b
    else:
        sum += A
print(sum)