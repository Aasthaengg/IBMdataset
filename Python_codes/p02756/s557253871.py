s = input()
p = int(input())

dir = 0
mae = []
usi = []

for _ in range(p):
  Q = input().split()
  if Q[0] == "1":
    dir = not dir
  else:
    if (int(Q[1]) - 1) == dir:
      mae.append(Q[2])
    else:
      usi.append(Q[2])
      
ans = "".join(mae[::-1]) + s + "".join(usi)
      
if not dir:
  print(ans)
else:
  print(ans[::-1])