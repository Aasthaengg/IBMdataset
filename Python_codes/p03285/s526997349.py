N = int(input())
List = []
for c in range(100//4 + 1):
  for d in range((100-4*c)//7 + 1):
    if 4*c + 7*d == N:
      List.append(c+d)
    else:
      continue
if bool(List) == True:
  print("Yes")
else:
  print("No")