n = int(input())
a = list(map(int,input().split()))
l,r = 0,0
ans = 0
s = 0
while l < n:
  if r < n and s+a[r] == s^a[r]:
    s += a[r]
    r += 1
    #print(s)
  else:
    ans += r-l
    s -= a[l]
    #print(s)
    l += 1
    
print(ans)