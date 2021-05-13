a,b,k = map(int, input().split())

ans = []
t = 0
for i in range(a,b+1):
  t += 1
  if t > k: break
  ans.append(i)
  
t = 0
for i in range(b,a-1,-1):
  t += 1
  if t > k: break
  ans.append(i)

for i in sorted(set(ans)): print(i)