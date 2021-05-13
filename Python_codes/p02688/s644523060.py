n, k = map(int, input().split())
d = [0]*k
a = [0]*k
for i in range(k):
  d[i] = int(input())
  a[i] = list(map(int, input().split()))
  
lis = [0]*n
for i in range(n):
  lis[i] = i + 1

alis = sum(a, [])

alis = list(set(alis))

for i in range(len(alis)):
  lis.remove(alis[i])
print(len(lis))