def con(n,d):
  if d == 0:
    return 1 / n
  else:
    return (n - d) * 2 / (n ** 2)

n,m,d = map(int, input().split())
beauty = con(n,d) * (m - 1)
print(beauty)