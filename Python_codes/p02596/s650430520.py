K = int(input())
L = 0
if K % 7 == 0:
  L = 9*K//7
else:
  L = 9*K
  
t = 1
ans = -1
for i in range(1,L,1):
  t = t*10
  if t % L == 1:
    ans = i
    break
  t = t % L
print(ans)