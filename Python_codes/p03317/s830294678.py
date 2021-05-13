n,k = map(int,input().split())
a = list(map(int,input().split()))
p = min(a)
a += [p]
ans,i,temp = 0,0,0
while i<n:
  if a[i]==p:
    m = -(-(i-temp)//(k-1))
    ans += m
    temp += m*(k-1)+1
    i = temp
  else:
    i += 1
ans += -(-(n-temp)//(k-1))
print(ans)