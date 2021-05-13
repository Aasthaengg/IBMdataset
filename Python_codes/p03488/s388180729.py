s = input()
x,y = map(int, input().split())
start = 0
key = len(s)
way = 0
dist = 0
now = 0
now_x = set([0])
now_y = set([0])
for k,i in enumerate(s):
  if i == "T":
    key = k
    break
  start += 1
x -= start
for i in s[key:]:
  if i == "T":
    if now:
      now = 0
      if way:
        new_y = set()
        for i in now_y:
          new_y.add(i+dist)
          new_y.add(i-dist)
        now_y = new_y
      else:
        new_x = set()
        for i in now_x:
          new_x.add(i+dist)
          new_x.add(i-dist)
        now_x = new_x
      dist = 0
    way ^= 1
  else:
    now = 1
    dist += 1
if way:
  new_y = set()
  for i in now_y:
    new_y.add(i+dist)
    new_y.add(i-dist)
    now_y = new_y
else:
  new_x = set()
  for i in now_x:
    new_x.add(i+dist)
    new_x.add(i-dist)
    now_x = new_x
if (x in now_x) and (y in now_y):
  print("Yes")
else:
  print("No")