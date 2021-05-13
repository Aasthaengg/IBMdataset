n = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(1,n-1):
  l = []
  l.append(p[i-1])
  l.append(p[i])
  l.append(p[i+1])
  ll = sorted(l)
  if ll[1] == p[i]:
    ans += 1
print(ans)