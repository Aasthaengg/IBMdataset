n = int(input())
xi = list(map(int,input().split()))
tairyoku = []
for p in range(100):
  tmp = 0
  for x in xi:
    tmp += (p+1-x)**2
  tairyoku.append(tmp)
print(min(tairyoku))
