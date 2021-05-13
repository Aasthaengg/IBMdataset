h,w,n = map(int, input().split())
ab = [tuple(map(int, input().split())) for i in range(n)]
J = [0] * 10
black = dict()
for i in ab:
  black[i] = 1
for a,b in ab:
  for x in range(max(0,3-a),min(3,h+1-a)):
    for y in range(max(0,3-b),min(3,w+1-b)):
      j = 0
      for X in range(a+x-2,a+x+1):
        for Y in range(b+y-2,b+y+1):
          if (X,Y) in black:
            j += 1
      J[j] += 1
for i in range(2,10):
  J[i] //= i
ALL = (h-2) * (w-2)
J[0] = ALL - sum(J[1:])
for i in J:
  print(i)