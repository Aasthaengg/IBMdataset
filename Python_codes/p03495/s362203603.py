import collections
n,k=map(int,input().split())
A=list(map(int,input().split()))
a=collections.Counter(A)
a=a.most_common()
cnt=0
for i in range(len(a)):
  if i>k-1:
    cnt+=a[i][1]
print(cnt)