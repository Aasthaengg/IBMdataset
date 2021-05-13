N = int(input())

d = {}
l = []
p = 0

for i in range(N):
  l.append(list(map(int, input().split())))

while True:
  if(l[0][2] == 0):
    l.append(l[0])
    del l[0]
  else:
    x, y, h= l[0]
    for i in range(101):
      for j in range(101):
        d[(i, j)] = abs(i- x)+ abs(j- y)+ h
    break

for k in range(N- 1):
  x, y, h = l[k+ 1]
  if(h == 0):
    for i in range(101):
      for j in range(101):
        if((i, j) in d):
          if(d[(i, j)]- abs(i- x)- abs(j- y)> 0):
            del d[(i, j)]
  else:
    for i in range(101):
      for j in range(101):
        if((i, j) in d):
          if(d[(i, j)] != abs(i- x)+ abs(j- y)+ h):
            del d[(i, j)]

zahyou, height = list(d.items())[0]
  
print("{0[0]} {0[1]} {1}".format(zahyou, height))