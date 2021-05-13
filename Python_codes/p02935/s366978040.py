n = int(input())

s = list(map(int, input().split()))

s.sort()

v = 0

if n == 1:
  print(s[0])
  exit()
elif n == 2:
  print((s[0]+s[1])/2)
  exit()

c = (s[0]+s[1])/2

del s[0]
del s[0]

for i in range(n-2):
  c = (c + s[0])/2
  del s[0]
  
  
print(c)