n, a, b = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
for i in range(n-1):
  if (l[i+1]-l[i])*a <= b:
    ans += (l[i+1]-l[i])*a
  else:
    ans += b
print(ans)