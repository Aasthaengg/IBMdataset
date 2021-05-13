k = int(input())
x = 7
ans = 1
if k%2 == 0 or k%5 ==0:
  print(-1)
  exit()
elif 7%k == 0:
  ans = 1

else:
  for i in range (1,k):
    x = (x*10+7)%k

    if x%k == 0:
      ans = i+1
      break

print(ans)

