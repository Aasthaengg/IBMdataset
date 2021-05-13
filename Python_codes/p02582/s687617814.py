r = list(input())
if r == ["R","S","R"] or r==["R","S","S"] or r==["S","S","R"] or r==["S","R","S"]:
  print(int(1))
elif r ==["R","R","S"] or r==["S","R","R"]:
  print(int(2))
elif r==["S","S","S"]:
  print(int(0))
else:
  print(int(3))