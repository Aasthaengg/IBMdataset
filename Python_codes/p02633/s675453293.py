X = int(input())
 
ans = 0
while(1):
  ans += 1
  if (X * ans) % 360 == 0:
    print(ans)
    break