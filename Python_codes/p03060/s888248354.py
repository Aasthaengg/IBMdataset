n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))
ans = 0
h = 0
while h < n:
  if v[h] >= c[h]:
    ans += v[h] - c[h]
  h += 1
print(ans)