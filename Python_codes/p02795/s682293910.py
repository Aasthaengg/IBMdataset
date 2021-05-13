h = int(input())
w = int(input())
n = int(input())
j = 0
k = 1
if h > w:
  j = h
else:
  j = w
while n > j:
  n = n - j
  k = k + 1
print(k)