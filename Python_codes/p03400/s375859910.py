n = int(input())
d, x = map(int, input().split())
c = [0 for i in range(d)]
a = []
for i in range(n):
  a.append(int(input()))

for i in range(n):
  tmp = 0
  while tmp * a[i] < d:
    c[tmp * a[i]] += 1
    tmp += 1
    
print(sum(c) + x)