n,w = map(int,input().split())
x = []
for i in range(n):
    x1,y1=[int(i) for i in input().split()]
    if i == 0:
      ti = x1
      zero = 0
      iti = 0
      ni = 0
      san = 0
    if x1 == ti:
      zero += 1
    elif x1 == ti+1:
      iti += 1
    elif x1 == ti+2:
      ni += 1
    else:
      san +=1
    x.append([x1,y1])
x.sort()
zer = x[:zero]
one = x[zero:iti+zero]
two = x[iti+zero:iti+ni+zero]
three = x[iti+ni+zero:zero+iti+ni+san]
zer.append([0,0])
one.append([0,0])
two.append([0,0])
three.append([0,0])
zer = sorted(zer,key = lambda x: -x[1])
one = sorted(one,key = lambda x: -x[1])
two = sorted(two,key = lambda x: -x[1])
three = sorted(three,key = lambda x: -x[1])
ans = 0
zer0 = [0]* len(zer)+ [0]
one0 = [0]* len(one)+ [0]
two0 = [0]* len(two)+ [0]
three0 = [0]* len(three)+ [0]
zerk = [0]* len(zer)+ [0]
onek = [0]* len(one)+ [0]
twok = [0]* len(two)+ [0]
threek = [0]* len(three)+ [0]
for i in range(1,len(zer)+1):
  zer0[i] = zer0[i-1] + zer[i-1][0]
  zerk[i] = zerk[i-1] + zer[i-1][1]
for i in range(1,len(one)+1):
  one0[i] = one0[i-1] + one[i-1][0]
  onek[i] = onek[i-1] + one[i-1][1]
for i in range(1,len(two)+1):
  two0[i] = two0[i-1] + two[i-1][0]
  twok[i] = twok[i-1] + two[i-1][1]
for i in range(1,len(three)+1):
  three0[i] = three0[i-1] + three[i-1][0]
  threek[i] = threek[i-1] + three[i-1][1]
for i in range(len(zer)):
  for j in range(len(one)):
    for k in range(len(two)):
      for l in range(len(three)):
        omo = zer0[i] + one0[j] + two0[k] + three0[l]
        kati  = zerk[i] + onek[j] + twok[k] + threek[l]
        if omo <= w:
          ans = max(ans,kati)
print(ans)