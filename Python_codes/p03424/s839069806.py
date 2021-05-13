n=input()
arares=input().split()
d = {'P': 0,
    'Y': 0,
    'W': 0,
    'G': 0}

for arare in arares:
  if arare in d:
    if d[arare]==0:
      d[arare]=1

colors = sum(d.values())
if colors == 3:
  print("Three")
elif colors == 4:
  print("Four")