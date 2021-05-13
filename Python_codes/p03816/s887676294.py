import collections
n=int(input())
s=list(map(int,input().split()))
k=len(collections.Counter(s))
if (n-k)%2==0:
    print(k)
else:
    print(k-1)