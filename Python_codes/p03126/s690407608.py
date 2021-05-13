x = list(map(int, input().split()))
k = [list(map(int, input().split())) for i in range(x[0])]
f = 0
for i in k:
  i.pop(0)
  if f == 0:
    tmp = i
    f = 1
    s = i
  else:
    s = set(tmp) & set(i)
    tmp = s
print(len(s))