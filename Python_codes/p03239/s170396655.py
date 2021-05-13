n = list(map(int, input().split()))
x = [list(map(int, input().split())) for i in range(n[0])]
ans = []
for i in x:
  if n[1] >= i[1]:
    ans.append(i[0])
if ans == []:
  print('TLE')
else:
  print(sorted(ans)[0])
