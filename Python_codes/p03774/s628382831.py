MM = input().split()
N = int(MM[0])
M = int(MM[1])
list1 = []
list2 = []
for i in range(N):
  LL = input().split()
  list1.append(LL)

for i in range(M):
  MM = input().split()
  list2.append(MM)

for i in list1:
  mini = 40**8
  ans = 0
  for j in range(len(list2)):
    x = int(i[0]) - int(list2[j][0])
    y = int(i[1]) - int(list2[j][1])
    xx = abs(x) + abs(y)
    if xx < mini:
      mini = xx
      ans = j+1
  print(ans)