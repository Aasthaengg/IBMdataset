k,t=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
print(max(2*a[0]-k-1,0))