n = int(input())

a_li = list(map(int, input().split()))

ans = 0
li = [0]*(n+1)

for i,a in enumerate(a_li):
  ans += (i+1)*a

for i,a in enumerate(a_li[::-1]):
  if i >= 1:
    li[i] = li[i-1]+a
  else:
    li[i] = a

li = li[::-1]

flag = True
ne = 0.5
for i in range(n+1):
  if li[i]  > 2*ne:
    ans -= li[i] -int(2*ne)

  
  ne = min(li[i] - a_li[i],int(2*ne)-a_li[i])

  if (i == n and ne != 0) or (i != n and ne <= 0):
    flag = False

  
if flag:
  print(ans)
else:
  print(-1)