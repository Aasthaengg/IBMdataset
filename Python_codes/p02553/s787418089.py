a, b, c, d = map(int, input().split())

lst = [ [a,b], [c,d] ]
mx = a*c
for i in range(2):
  x = lst[0][i]*lst[1][0]
  if x >= mx:
    mx = x
  x = lst[0][i]*lst[1][1]
  if x >= mx:
    mx = x
print(mx)