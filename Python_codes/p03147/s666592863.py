n = int(input())
h = list(map(int,input().split()))
g = [0]*n
ans = 0
l = 0
while not h == g:
  if not g[l] == h[l]:
    r = l+1
    while r <= n-1 and not g[r] == h[r]:
      r += 1
    #lは水やりが必要な左端、rはlより右で水やりが必要ない左端
    for i in range(l,r):
      g[i] += 1
    ans += 1
  if g[l] == h[l]:
    l += 1
print(ans)