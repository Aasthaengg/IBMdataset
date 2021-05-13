n = int(input())
b = [int(i) for i in input().split()]
le = n
ans = []
for i in range(n):
  for j,bj in enumerate(b[::-1]):
    if j+bj > le:
      print(-1)
      exit()
    if j+bj == le:
      ans.append(bj)
      b = b[:le-j-1]+b[le-j:]
      le -= 1
      break
      
for i in ans[::-1]:
  print(i)