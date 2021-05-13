a,b,k = map(int, input().split())
i = 1
l = []
while i <= min(a,b):
  if a%i == 0 and b%i == 0:
    l.append(i)
  i += 1
print(l[len(l)-k])