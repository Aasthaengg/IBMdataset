n,k = map(int, input().split())
a = list(map(int, input().split()))
if (n==k):
    print(1)
else:
    print(1+(n-k-1)//(k-1)+1)