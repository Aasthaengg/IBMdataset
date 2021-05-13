n = input()
s = len(n)-1


for i in range(2**s):
  op = ""
  for j in range(s):
    if (i>>j)&1:
      op += "+"
    else:
      op += "-"
  ans =int(n[0])
  for j in range(len(op)):
    if op[j]=="+":
      ans += int(n[j+1])
    else:
      ans -= int(n[j+1])
  if ans == 7:
      ret = ""
      for k in range(len(op)):
        ret += n[k]
        ret += op[k]
      ret += n[-1]
      ret += "=7"
      print(ret)
      exit(0)