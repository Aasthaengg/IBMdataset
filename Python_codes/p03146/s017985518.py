def calc(a):
  if a % 2 == 0:
    return int(a / 2)
  else:
    return 3 * a + 1

s = int(input())
c = 1
n = s
l = [s]

while True:
  m = calc(n)
  if l.count(m) == 1:
    break
  l.append(m)
  c += 1
  n = m
   
print(c+1)