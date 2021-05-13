N, K = input().split(sep=' ')
p = list(input().split(sep=' '))
p = list(map(int, p))
p.sort()
buy = 0
for item in range(int(K)):
  buy += p[item]
print(buy)