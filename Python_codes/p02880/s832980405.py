n=int(input())
s=set()
for i in range(1,10):
  for j in range(1,10):
    p=i*j
    s.add(p)
if n in s:
  print("Yes")
else:
  print("No")