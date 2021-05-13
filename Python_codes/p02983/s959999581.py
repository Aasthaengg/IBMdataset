L,R = map(int, input().split())
l = L//2019
r = R//2019
m = L%2019
n = R%2019

ans = 2018
if l != r:
  print(0)
  exit()
else:
  for i in range(m,n):
    for j in range(i+1,n+1):
      ans = min((i*j) % 2019, ans)
      if ans == 0:
        print(ans)
        exit()
      
print(ans)
