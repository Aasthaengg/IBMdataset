n, k = map(int, input().split())
ans = n**2
for b in range(1, n+1):
  if b > k:
    ans -= (n//b)*k+min([n%b, max([k-1, 0])])
  else:
    ans -= n
print(ans)