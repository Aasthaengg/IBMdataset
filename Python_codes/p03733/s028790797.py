n,t=map(int,input().split())
a=list(map(int,input().split()))
souwa=0
for i in range(1,n):
    souwa+=min(a[i]-a[i-1],t)
print(souwa+t)