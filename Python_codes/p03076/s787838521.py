m = [input()for i in range(5)]

ma = 0
for i in range(1,5):
  if m[i][-1] == '0':
    continue
  if int(m[ma][-1]) > int(m[i][-1]):
    ma = i
c = 0
for i in range(5):
  tmp = int(m[i])
  if i != ma and tmp % 10 !=0:
    tmp = tmp // 10 * 10 + 10
  c += tmp
print(c)                      