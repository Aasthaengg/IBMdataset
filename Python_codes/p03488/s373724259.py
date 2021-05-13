S = input()
XX,YY= [ int(it) for it in input().split() ]


s = 0
li=[]
for v in S:
  if (v=='T'):
    li.append(s)
    s = 0
  else:
    s += 1
li.append(s)
    
liv = li[1:]
liy = liv[0::2]
lix = liv[1::2]

xset = set([li[0]])
for v in lix:
  tmp = set()
  for w in xset:
    tmp.add(+v+w)
    tmp.add(-v+w)
  xset = tmp

yset = set([0])
for v in liy:
  tmp = set()
  for w in yset:
    tmp.add(+v+w)
    tmp.add(-v+w)
  yset = tmp

if ( XX in xset and YY in yset ):
  print ("Yes")
else:
  print ("No")