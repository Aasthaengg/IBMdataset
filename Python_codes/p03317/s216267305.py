n,k = map(int,input().split())
a = list(map(int, input().split()))
print((n-1)//(k-1)+((n-1)%(k-1)>0))