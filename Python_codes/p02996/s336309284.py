n=int(input())
ab=[list(map(int,input().split())) for i in range(n)]
ab.sort(key=lambda x: x[1])
t=0
for x in ab:
  if t+x[0] <= x[1]:
    t += x[0]
  else:
    print('No')
    break
else:
  print('Yes')
