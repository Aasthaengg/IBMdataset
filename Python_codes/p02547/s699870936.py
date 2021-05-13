n = int(input())
p = [list(map(int, input().split())) for i in range(n)]

ans = 0
ck = 0

for i in range(n):
  if p[i][0] == p[i][1]:
    ans += 1
    if ans == 3:
      ck = 1
      print("Yes")
      break
  else:
    ans = 0
    
if ck == 0:
  print("No")