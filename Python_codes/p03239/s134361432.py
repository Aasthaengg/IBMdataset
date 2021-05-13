n, t = map(int, input().split())
lst = []
for i in range(n):
  tp = tuple(map(int, input().split()))
  if tp[1] <= t:
    lst.append(tp)
if lst == []:
  print('TLE')
  exit()
print(min(lst, key=lambda x: x[0])[0])