N = int(input())
MAX = 500
A = [[1],[1]] #size = 2
#A = [[1,2],[2,3],[3.1]]
size = 0
for i in range(1,MAX):
  if i*(i+1)//2 == N:
    size = i+1
    break
if size == 0:
  print("No")
  exit()
now = 2
while now < size:
  start = now*(now-1)//2+1
  last = [start+i for i in range(now)]
  for j in range(len(A)):
    A[j].append(last[j])
  A.append(last)
  now += 1
print("Yes")
print(len(A))
#ini = [len(A)-1]
for x in A:
  x.insert(0,len(A)-1)
  print(*x)