S = input()
T = input()
flag = False

def irekae(s):
  List = list(s)
  a = List.pop(0)
  List.append(a)
  res = ""
  for i in range(len(s)):
    res += List[i]
  return res

if S == T:
  flag = True
else:
  for i in range(len(S)):
    S = irekae(S)
    if S == T:
      flag = True
      break
if flag:
  print("Yes")
else:
  print("No")