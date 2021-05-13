n = int(input())
if n==1:
  c=int(input())
  print(c)
  print(c)
  quit()
line = [list(map(int, input().split())) for i in range(n-1)]
c = list(map(int, input().split()))
c.sort(reverse=True)
print(sum(c)-c[0])
ans=[0]*n
vis=[True]*n
a, b = line[0]
a-=1
b-=1
ans[a]=c[0]
ans[b]=c[1]
vis[a]=False
vis[b]=False
for i in range(1, n-1):
  for l in line:
    a, b = l
    a-=1
    b-=1
    if (vis[a] and (not vis[b])):
      ans[a]=c[i+1]
      vis[a]=False
      break
    elif (vis[b] and (not vis[a])):
      ans[b]=c[i+1]
      vis[b]=False
      break
#print(ans)
ans = list(map(str, ans))
print(" ".join(ans))