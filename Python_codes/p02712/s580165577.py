N = int(input())
ans = 0
for i in range(N+1):
  if i%15 == 0 or i%5 == 0 or i%3 ==0:
    ans += 0
  else:
    ans += i
print(ans)