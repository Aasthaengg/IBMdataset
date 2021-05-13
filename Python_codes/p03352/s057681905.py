x=int(input())

s=set([1])

for b in range(2,x):
  for p in range(2,11):
    if b**p>x:
      break
    s.add(b**p)
print(max(s))