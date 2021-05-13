S = input()
List = list(S)
s_l = set(List)
n = 10
res= ""
flag = False
for i in range(97,123):
  if not chr(i) in s_l:
    res = chr(i)
    flag = True
    break
if flag:
  print(res)
else:
  print("None")