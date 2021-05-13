s = input()
X, Y = map(int, input().split())
fs = s.split("T")
nsx = list(map(len, fs[0::2]))
nsy = list(map(len, fs[1::2]))
ssx = []
ssx.append({ 0 })
ssx.append({ nsx[0] })
for i in range(1, len(nsx)):
  s = ssx[i]
  n = nsx[i]
  s2 = set()
  for x in s:
    s2.add(x+n)
    s2.add(x-n)
  ssx.append(s2)
#print(ssx)
ssy = [{ 0 }]
for i in range(0, len(nsy)):
  s = ssy[i]
  n = nsy[i]
  s2 = set()
  for y in s:
    s2.add(y+n)
    s2.add(y-n)
  ssy.append(s2)
#print(ssy)
if X in ssx[-1] and Y in ssy[-1]:
  print("Yes")
else:
  print("No")
