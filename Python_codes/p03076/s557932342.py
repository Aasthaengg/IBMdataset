List = []
for i in range (5):
  List.append(int(input()))
res = 10
n = 0
calc = 0
RES = 0
for i in range(5):
  n = List[i]%10
  RES += List[i]
  if n == 0:
    pass
  else:
    res = min(n,res)
    calc += 10-n
RES = RES + calc -10 + res
print(RES)