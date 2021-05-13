n = int(input())
b = list(map(int,input().split()))
a = []
for i in range(n,0,-1):
  flag = 1
  for j in range(i-1,-1,-1):
    if b[j] == j+1:
      a.append(b.pop(j))
      flag = 0
      break
  if flag:
    print(-1)
    quit()
for i in a[::-1]:
  print(i)