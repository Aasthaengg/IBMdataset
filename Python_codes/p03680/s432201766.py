N = int(input())

A = []

for i in range(N):
  a = int(input())
  A.append(a-1)
  
seen = set()

pos = 0
seen.add(0)
count = 0
while pos != 1:
  pos = A[pos]
  if pos in seen:
    count = -1
    break
  else:
    seen.add(pos)
  count += 1
  
print(count)