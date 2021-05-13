n,k = map(int,input().split())
a = list(map(int,input().split()))
for j in range(k,n):
    if a[j-k] < a[j]:
        print('Yes')
    else:
        print('No')
