n,m= map(int, input().split())
h = list(map(int, input().split()))
t = [0]*(n+1)
ans = 0
for i in range(m):
  a,b = map(int, input().split())
  if h[a-1]==h[b-1]:
    t[b]+=1
    t[a]+=1
  elif h[a-1]>h[b-1]:
    t[b]+=1
  elif h[a-1]<h[b-1]:
    t[a]+=1

for i in range(1,n+1):
  if t[i] == 0:
    ans +=1
print(ans)