x = list(map(int, input().split()))
n = [list(map(int, input().split())) for i in range(2)]
a = sorted(n[0], reverse=True)[0]
b = sorted(n[1])[0]
war = 0
for i in range(x[2]+1, x[3]):
  if (i > a) and (i <= b):
    war = 1
if war == 1:
  print('No War')
else:
  print('War')
