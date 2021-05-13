n = int(input())
k = int(input())
m = 1
for i in range(n):
  m += min(m, k)
print(m)