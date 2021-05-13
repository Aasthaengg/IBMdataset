s = input()
l = []
for i in range(len(s)-2):
  n = int(s[i:i+3])
  l.append(abs(753-n))
print(min(l))