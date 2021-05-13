A,B,C = map(int, input().split())

if A==B and B!=C:
  print("Yes")
  exit()
  
if B==C and C!=A:
  print("Yes")
  exit()
  
if A==C and C!=B:
  print("Yes")
  exit()

print("No")