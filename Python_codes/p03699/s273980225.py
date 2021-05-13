n = int(input())
s = []
for i in range(n):
  s_ = int(input())
  s.append(s_)

s.sort() 
total = sum(s)
t = [i for i in s if i % 10 != 0]
if total % 10 != 0:
  print(total)
elif len(t) > 0:
  print(total - t[0])
else:
  print(0)