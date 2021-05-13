n = int(input())
d = []
ans = 0
for i in range(n):
  d_ = int(input())
  if d_ not in d:
    d.append(d_)
    ans += 1
print(ans)