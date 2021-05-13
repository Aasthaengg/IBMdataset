x = list(map(str, input()))
for i in range(2**3):
  op = ["-","-","-"]
  for j in range(3):
    if (i & 1<<j):
      op[j] = "+"
  if eval(x[0]+op[0]+x[1]+op[1]+x[2]+op[2]+x[3]) == 7:
    print(x[0]+op[0]+x[1]+op[1]+x[2]+op[2]+x[3]+"=7")
    break