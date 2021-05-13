n = int(input())
L = list(map(int,input().split()))
L.sort()
T = []
plus = []
minus = []
for i in range(n):
  if L[i] >= 0:
    plus.append(L[i])
  else:
    minus.append(L[i])
if len(L) == 2:
  if len(plus) == len(minus):
    print(plus[0]-minus[0])
    print(plus[0],minus[0])
  elif len(plus) == 2:
    print(plus[1]-plus[0])
    print(plus[1],plus[0])
  else:
    print(minus[1]-minus[0])
    print(minus[1],minus[0])
else:
  if len(plus) != 0 and len(minus) != 0:
    if min(len(plus),len(minus)) >= 2:
      T.append([minus[0],plus[0]])
      cur = minus[0]-plus[0]
      for i in range(1,len(plus)-1):
        T.append([cur,plus[i]])
        cur = cur-plus[i]
      T.append([plus[len(plus)-1],cur])
      cur = plus[len(plus)-1]-cur
      for i in range(1,len(minus)):
        T.append([cur,minus[i]])
        cur = cur-minus[i]
      print(cur)
      for i in range(len(T)):
        print(T[i][0],T[i][1])
    else:
      if len(minus) == 1:
        cur = minus[0]
        T.append([cur,plus[0]])
        cur = cur-plus[0]
        for i in range(1,len(plus)-1):
          T.append([cur,plus[i]])
          cur = cur-plus[i]
        T.append([plus[len(plus)-1],cur])
        cur = plus[len(plus)-1]-cur
        print(cur)
        for i in range(len(T)):
          print(T[i][0],T[i][1])
      else:
        cur = plus[0]
        T.append([cur,minus[0]])
        cur = cur-minus[0]
        for i in range(1,len(minus)):
          T.append([cur,minus[i]])
          cur = cur-minus[i]
        print(cur)
        for i in range(len(T)):
          print(T[i][0],T[i][1])
  elif len(plus) == 0:
    cur = minus[len(minus)-1]
    for i in range(n-1):
      T.append([cur,minus[n-i-2]])
      cur = cur-minus[n-i-2]
    print(cur)
    for i in range(len(T)):
      print(T[i][0],T[i][1])
  else:
    cur = plus[0]
    for i in range(1,n-1):
      T.append([cur,plus[i]])
      cur = cur-plus[i]
    T.append([plus[n-1],cur])
    cur = plus[n-1]-cur
    print(cur)
    for i in range(len(T)):
      print(T[i][0],T[i][1])