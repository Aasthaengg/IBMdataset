n = int(input())
v = sorted(list(map(int, input().split())))

while True:
  ans = 0
  ans += (v[0] + v[1])/2
  if len(v) == 2:
    break
  else:
    v.pop(0)
    v.pop(0)
    v.insert(0, ans)
print(ans)