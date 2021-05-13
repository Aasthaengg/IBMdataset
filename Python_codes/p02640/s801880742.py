x, y = [int(x) for x in input().split()]

ans = 'No'

for tsuru in range(x+1):
  kame = x - tsuru
  if tsuru * 4 + kame * 2 == y:
    ans='Yes'
  else:
    pass

print(ans)