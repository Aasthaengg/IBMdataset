N =int(input())
List = list(map(int, input().split()))
flag = True
res = 0
while flag:
  for i in range(N):
    if List[i] % 2 == 1:
      flag = False
      break
    else:
      List[i] = List[i]//2
  if flag:
    res += 1
print(res)