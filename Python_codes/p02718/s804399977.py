a,b=map(int,input().split())
List = list(map(int, input().split()))
wa = 0
List.sort(reverse = True)
for i in range(a):
  wa += List[i]
thresi = wa / (4 * b)
flag = False
for i in range(b):
  if List[i] >= thresi:
    flag = True
  else:
    flag = False
if flag:
  print("Yes")
else:
  print("No")