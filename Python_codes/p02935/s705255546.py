n = int(input())
lis = list(map(int, input().split()))
lis.sort()
x = 0
y = 0

for i in range(n):
  if i == 0:
    x = lis[i]
  else:
    x = (x + lis[i]) / 2
    
print(x)