S = list(input())

for i in range(2**3):
  ans = int(S[0])
  res = ["-","-","-"]
  for j in range(3):
    if ((i >> j) & 1):
      ans += int(S[j+1])
      res[j] = "+"
    else:
      ans -= int(S[j+1])
  if ans == 7:
    print(S[0]+res[0]+S[1]+res[1]+S[2]+res[2]+S[3]+"=7")
    exit()