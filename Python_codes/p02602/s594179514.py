n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(n-k):
    print('Yes' if l[i]<l[i+k] else 'No')