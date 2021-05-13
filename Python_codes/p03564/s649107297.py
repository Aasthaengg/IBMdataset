n = int(input())
k = int(input())
s = 1
while n > 0:
  if s < k:
    s = s*2
  else:
    s += k
  n -= 1
print(s)