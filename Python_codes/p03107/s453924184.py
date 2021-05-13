s = input()
n = len(s)
m = 0
for x in s:
  m += int(x)
print(n-abs(n-2*m))