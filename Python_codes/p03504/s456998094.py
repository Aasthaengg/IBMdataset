#14:29
n,cn = map(int,input().split())
event = []
for _ in range(n):
  s,t,c = map(int,input().split())
  event.append([s-1,1,c-1])
  event.append([t  ,0,c-1])
event.sort()
can = []
now = 0
chan = [0 for _ in range(cn)]
for x in event:
  u,i,c = x
  if chan[c] == 0 and i == 1:
    chan[c] += 1
    now += 1
    can.append(now)
  elif chan[c] == 1 and i == 1:
    chan[c] += 1
  elif chan[c] == 1 and i == 0:
    chan[c] -= 1
    now -= 1
  elif chan[c] == 2 and i == 0:
    chan[c] -= 1
  else:
    print(fuck)
  #print(chan,u)
print(max(can))