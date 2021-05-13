n,k = map(int,input().split())
if k > n*(n-1)//2 - (n-1):
  print(-1)
  quit()
g = [[1,i+1] for i in range(1,n)]
t = (n-1)*(n-2)//2
for i in range(2,n):
  for j in range(i+1,n+1):
    if t == k:
      print(len(g))
      for l in g:
        print(*l)
      quit()
    g.append([i,j])
    t -= 1
print(len(g))
for l in g:
  print(*l)