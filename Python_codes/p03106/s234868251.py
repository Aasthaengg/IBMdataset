a, b, c = map(int, input().split())
i = 1
d = []
while True:
  if a % i ==0 and b % i ==0:
    d.append(i)
  if i > max(a,b):
    break
  else:
    i += 1
print(d[-c])