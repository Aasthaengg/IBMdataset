n=int(input())
a=list(map(int,input().split()))
a=sorted(a,reverse=True)
print(a[0]-a[n-1])
