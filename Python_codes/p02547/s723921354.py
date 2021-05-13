N = int(input())

cons = 0
for i in range(N):
  val = [int(x) for x in input().split()]
  if val[0] == val[1]: cons += 1
  else: cons = 0
  if cons == 3:
    print('Yes')
    break
else: print('No')