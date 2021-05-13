n = int(input())
l = [2,1]
l = l + [0]*(n-1)
if n == 1:
  print(1)
  exit()
for i in range(2,n+1):
  l[i] = l[i-2] + l[i-1]
print(l[n])