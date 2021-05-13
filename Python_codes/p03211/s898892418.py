from sys import stdin

s = stdin.readline().strip()
d = 100000000000

for i in range(len(s)-2):
  obj = int(s[i:i+3])
  if abs(753 - obj) < d:
    d = abs(753 - obj)
    
print(d)