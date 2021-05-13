n = int(input())
t = list(map(int, input().split()))
r = {}
ans = 0
for i in range(len(t)):
  try:
    r[i+1 + t[i]] += 1
  except KeyError:
    r[i+1 + t[i]] = 1
for i in range(len(t)):
  if((i+1 - t[i]) >= 1):
    try:
      ans += r[i+1-t[i]]
    except KeyError:
      continue
print(ans)
