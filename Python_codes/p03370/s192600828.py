MM = input().split()
N = int(MM[0])
X = int(MM[1])
mini = 1000
for i in range(N):
  a = int(input())
  X -= a
  if mini > a:
    mini = a
count = 0

while X >= mini:
  count +=1
  X -= mini
print(count + N)