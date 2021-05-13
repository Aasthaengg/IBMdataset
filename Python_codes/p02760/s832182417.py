A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))
A3 = list(map(int,input().split()))

N = int(input())
A10,A11,A12,A20,A21,A22,A30,A31,A32 = 0,0,0,0,0,0,0,0,0
for n in range(N):
  b = int(input())
  
  if A1[0] == b:
    A10 += 1
  elif A1[1] == b:
    A11 += 1
  elif A1[2] == b:
    A12 += 1
  elif A2[0] == b:
    A20 += 1
  elif A2[1] == b:
    A21 += 1
  elif A2[2] == b:
    A22 += 1
  elif A3[0] == b:
    A30 += 1
  elif A3[1] == b:
    A31 += 1
  elif A3[2] == b:
    A32 += 1

if A10+A11+A12 == 3:
  print("Yes")
elif A20+A21+A22 == 3:
  print("Yes")
elif A30+A31+A32 == 3:
  print("Yes")
elif A10+A20+A30 == 3:
  print("Yes")
elif A11+A21+A31 == 3:
  print("Yes")
elif A12+A22+A32 == 3:
  print("Yes")
elif A10+A21+A32 == 3:
  print("Yes")
elif A12+A21+A30 == 3:
  print("Yes")
else:
  print("No")