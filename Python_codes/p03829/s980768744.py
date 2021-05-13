n,a,b=map(int,input().split())
x=list(map(int,input().split()))
print(sum(min(a*(x[i+1]-x[i]),b) for i in range(n-1)))