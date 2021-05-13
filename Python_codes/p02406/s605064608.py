n = int(input())
ans = ''
for i in range(1, n+1):
 if i%3 == 0:
  ans += " " + str(i)
 elif i%10 == 3:
  ans += " " + str(i)
 else:
  div = i
  while div//10:
   div = div//10
   if div%10 == 3:
    ans += " " + str(i)
    div = 0
print(ans)