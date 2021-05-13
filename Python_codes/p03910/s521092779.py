n = int(input())
l = []
s = 0
for i in range(1,10**7+1):
  if n>=s:
    s += i
    l.append(i)
  else:
    break
if s-n>0:
  a = s-n
  l.remove(a)
for i in l:
  print(i)