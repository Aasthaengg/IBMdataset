s = input()
s1 = [i for i in s]
c = 700
for i in range(3):
  if "o" == s1[i]:
    c += 100
  else:
    c += 0
print(c)