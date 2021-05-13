L = [[1, 3, 5, 7, 8, 10, 12],[4, 6, 9, 11],[2]]
x, y = map(int,input().split())
ans = False
for i in range(len(L)):
  if x in L[i] and y in L[i]:
    ans = True
if ans:
  print("Yes")
else:
  print("No")
