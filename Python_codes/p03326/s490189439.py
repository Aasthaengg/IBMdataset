n,m = map(int,input().split())
raw = []
for _ in range(n):
  raw.append(list(map(int,input().split())))
time = [0,0,0]
def nex(t):
  for d in range(3):
    if t[d] == 0:
      t[d] = 1
      return t
    else:
      t[d] = 0
  else:
    return 'over'
can = []
while time != 'over':
  now = []
  for i in range(n):
    tmp = 0
    for d in range(3):
      if time[d] == 0:
        tmp += raw[i][d]
      else:
        tmp -= raw[i][d]
    now.append(tmp)
  now.sort(reverse=True)
  can.append(sum(now[:m]))
  time = nex(time)
print(max(can))