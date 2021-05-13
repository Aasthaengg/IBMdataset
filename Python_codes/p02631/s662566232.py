n = int(input())
a = list(map(int,input().split()))
b = [0]*(n-1)
ans = a[0]
for i in range(1,n):
  b[i-1] = a[0]^a[i]
  ans ^= b[i-1]
print(ans,end=' ')
for i in range(1,n):
  print(ans^b[i-1],end=' ')