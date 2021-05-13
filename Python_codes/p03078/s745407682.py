x,y,z,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

AB = []
for xi in range(x):
  for yi in range(y):
    AB.append(A[xi]+B[yi])

AB = sorted(AB,reverse=True)
C = sorted(C,reverse=True)

i=0
j=0

ABC = []
for ab in AB[:k]:
  for c in C[:k]:
    ABC.append(ab+c)

ABC = sorted(ABC,reverse=True)
for abc in ABC[:k]:
  print(abc)