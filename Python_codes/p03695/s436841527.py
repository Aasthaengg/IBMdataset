N = int(input())
A = list(map(int,input().split()))
color = set([])
select = 0
for i in range(N):
  if A[i] <= 399:
    color.add(0)
  elif A[i] <= 799:
    color.add(1)
  elif A[i] <= 1199:
    color.add(2)
  elif A[i] <= 1599:
    color.add(3)
  elif A[i] <= 1999:
    color.add(4)
  elif A[i] <= 2399:
    color.add(5)
  elif A[i] <= 2799:
    color.add(6)
  elif A[i] <= 3199:
    color.add(7)  
  else:
    select += 1

if select == N:
  print(1,select)
  exit()
MIN = len(color)
MAX = MIN + select
print(MIN,MAX)