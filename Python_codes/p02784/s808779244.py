n,k=map(int,input().split())
a=list(map(int,input().split()))

a.sort(reverse=True)

s=0

for i in range(k):
  s+=a[i]

print('Yes' if s >= n else 'No')