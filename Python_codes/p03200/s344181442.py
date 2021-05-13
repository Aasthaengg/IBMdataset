S = input()

tmp = 0
rlt = 0

for s in S:
  if s == "B":
    tmp += 1
  else:
    rlt += tmp
    
print(rlt)