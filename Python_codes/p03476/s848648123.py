import bisect
L = []
for _ in range(int(input())):
  a, b = map(int, input().split())
  a, b = (a-1)//2, (b-1)//2
  L.append([a,b])
X_1 = [i for i in range(2, 10**5+1)]
X_2 = []
while len(X_1)>0:
  X_2.append(X_1[0])
  X_1 = [x for x in X_1 if x%X_1[0] != 0]
T = [0]*(10**5)
for i in range(10**5-1):
  if bisect.bisect_left(X_2, 2*i+1)!=bisect.bisect_right(X_2, 2*i+1)\
  and bisect.bisect_left(X_2, i+1)!=bisect.bisect_right(X_2, i+1):
    T[i+1]=T[i]+1
  else:
    T[i+1]=T[i]
for l in L:
  print(T[l[1]+1]-T[l[0]])