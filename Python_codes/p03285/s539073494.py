n = int(input())
quotient = n // 4
rep = [4*i for i in range(quotient+1)]
flag = False
while rep[0] <= n:
  if n in rep:
    print('Yes')
    flag = True
    break
  rep = [7+ele for ele in rep]

if not flag:
  print('No')