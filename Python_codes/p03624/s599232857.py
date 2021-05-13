L = [chr(i) for i in range(97, 123)]
f = 0
s = input()
for l in L:
  if s.count(l) == 0:
    print(l)
    f = 1
    break
if f == 0:
  print("None")