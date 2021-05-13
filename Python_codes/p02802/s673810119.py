n,m = map(int, input().split())

prob = {}


for i in range(m):
  x,y = input().split()
  if x not in prob:
    if y == 'AC':
      prob[x] = [1, 0]
    else:
      prob[x] = [0, 1]
  else:
    if prob[x][0] == 0:
      if y == 'AC':
        prob[x][0] += 1
        answered = True
      else:
        prob[x][1] += 1

ac = 0
wa = 0

for i in prob:
  if prob[i][0] == 1:
    ac += 1
    wa += prob[i][1]

print(ac, wa)