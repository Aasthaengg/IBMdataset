n = int(input())
l = sorted(map(int, input().split()))
a = 0
b = 0
for i in range(n):
  if i % 2 == 0:
  	a += l.pop()
  else:
    b += l.pop()
print(a - b)