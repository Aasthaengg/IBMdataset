n = int(input())
a = list(map(int,input().split()))

p = 1

for i in range(n):
  if a[i] == 0:
    print(0)
    exit()

for j in range(n):
  p *= a[j]
  if p > 10**18:
    print(-1)
    exit()

print(p)