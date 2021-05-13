S = list(input())
d = dict()
for i in S:
  if not i in d:
    d[i] = 1
  else:
    d[i] += 1

res = "Yes"
for i in d.values():
  if i != 2:
    res = "No"
    break
print(res)