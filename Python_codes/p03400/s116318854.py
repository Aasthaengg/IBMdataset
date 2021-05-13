n = int(input())
d, x = map(int, input().split())
an = []
for i in range(n):
  an.append(int(input()))

choco = []
for i in range(n):
  j = 0
  count = 0
  while(True):
    if 1+an[i]*j <= d:
      count += 1
      j += 1
    else :
      choco.append(count)
      break
      
choco.append(x)
      
print(sum(choco))