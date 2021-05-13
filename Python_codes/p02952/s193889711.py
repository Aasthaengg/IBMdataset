n = int(input())
l = len(str(n))
s = 0
for i in range(l//2):
  s += 9*(10**(2*i))
if l % 2==0:
  print(s)
  exit()

d = n - 10**(l-1)
print(s+d+1)
