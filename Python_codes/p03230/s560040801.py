n = int(input())
k = int((n*2)**.5)
if k*(k+1)//2 != n:
  print("No")
  exit()
print("Yes")
print(k+1)
l = [set() for _ in range(k+1)]
t = 0
for i in range(k):
  for j in range(i+1):
    t += 1
    l[i].add(t)
    l[j].add(t)
  l[-1].add(t)
for x in l:
  print(k," ".join(map(str,x)))