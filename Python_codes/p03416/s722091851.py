A, B = map(int,input().split())
r = B - A +1
ans = 0
for i in range(r):
  n = str(A + i)
  l = len(n)//2
  count = 0
  for j in range(l):
    if n[j] == n[-(j+1)]:
      count +=1
  if count == l:
    ans += 1
    
print(ans)