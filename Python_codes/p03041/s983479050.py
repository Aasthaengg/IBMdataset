n, k = map(int, input().split())
s = input()
res = []
for i in s:
  res.append(i)
if res[k-1] == 'A':
  res[k-1] = 'a'
elif res[k-1] == 'B':
  res[k-1] = 'b'
else:
  res[k-1] = 'c'
print(*res, sep='')