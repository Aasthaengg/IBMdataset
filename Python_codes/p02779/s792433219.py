n = int(input())
tmp = input().split()
a = []
for i in range(n):
  a.append(int(tmp[i]))

a.sort()

for i in range(n-1):
  x = a[i]
  y = a[i+1]
  if(x == y):
    print("NO")
    exit()

print("YES")