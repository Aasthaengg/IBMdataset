n,c,k = map(int,input().split())
t = []
for i in range(n):
  t.append(int(input()))

t.sort()
ans = 0
now = 0
ter = -1
for i in range(n):
  if ter < t[i]:
    ans += 1
    ter = t[i]+k
    now = 1
  else:
    if(c<=now):
      ans+=1
      ter = t[i]+k
      now = 1
    else:
      now += 1
      
print(ans)