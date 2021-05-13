x, n = map(int, input().split())
y = list(map(int, input().split()))
a = x
for i in range(100):
  if (x-i) not in y:
    a = x-i
    break
  if (x+i) not in y:
    a = x+i
    break
print(a)