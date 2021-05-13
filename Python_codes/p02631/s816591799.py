n = int(input())
a = list(map(int,input().split()))

all_xor = a[0]

for i in range(1,n):
  all_xor = all_xor ^ a[i]
  
ans = [a[i] ^ all_xor for i in range(n)]

for i in range(n):
  print(ans[i],end=' ')