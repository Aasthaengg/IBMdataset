a,b = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
for i in range(a):
  if b <= l[i]:
    ans += 1
print(ans)
