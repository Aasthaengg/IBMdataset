n,k=map(int,input().split())
x=list(map(int,input().split()))
l=[]
for i in range(n-k+1): l.append(x[i+k-1]-x[i]+min(abs(x[i]),abs(x[i+k-1])))
print(min(l))