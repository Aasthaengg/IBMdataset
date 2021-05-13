n,k=map(int,input().split())
x=list(map(int,input().split()))
print(min([x[i+k-1]-x[i]+min(abs(x[i]),abs(x[i+k-1])) for i in range(n-k+1)]))