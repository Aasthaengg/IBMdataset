d = {}
n = input()
aaa = list(map(int, input().split(' ')))
ans = 'YES'
for a in aaa:
  d[a] = d.get(a, 0) + 1
  if d[a] >= 2:
    ans = 'NO'
print(ans)
