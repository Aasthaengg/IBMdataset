n=int(input())//2
a= list(map(int,input().split()))
a=sorted(a)
print(a[n]-a[n-1])