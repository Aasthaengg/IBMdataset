n = int(input())
ans = set()
if n%2 == 1:
  for i in range(1,n):
    ans.add((i,n))
  n -= 1
if n%2 == 0:
  chk = [[] for i in range(n//2)]
  for i in range(1,n//2+1):
    chk[i-1].append(i)
    chk[i-1].append(n+1-i)
  for i in range(n//2-1):
    for j in range(2):
      a = chk[i][j]
      for k in range(i+1,n//2):
        b = chk[k][0]
        c = chk[k][1]
        if a < b:
          ans.add((a,b))
        else:
          ans.add((b,a))          
        if a < c:
          ans.add((a,c))
        else:
          ans.add((c,a))
          
#print(ans)
print(len(ans))
for i in ans:
  print(*i)