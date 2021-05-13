S = input()
A,B,C = map(int,S.split())

if A==B and B==C:
  print("No")
elif A==B or A==C or B==C:
  print("Yes")
else:
  print("No")