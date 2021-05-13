a = list(map(int, input().split()))
K = int(input())

for i in range(K):
  x = a.index(max(a))
  a[x] *= 2
  i += 1
  
print(sum(a))
