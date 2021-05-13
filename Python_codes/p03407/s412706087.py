ABC = input()
ABC = list(ABC.split())

A = int(ABC[0])
B = int(ABC[1])
C = int(ABC[2])

if A+B >= C:
  print('Yes')
else:
  print("No")