a = int(input())
b = int(input())
c = int(input())
d = int(input())

tr = 0
bu = 0

if a < b:
  tr = a
else:
  tr = b
  
if c < d:
  bu = c
else:
  bu = d
print(tr + bu)