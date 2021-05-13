N = int(input())
rabit = [ int(v) for v in input().split(" ") ]
skip = set()
num = 0
 
for i in range(N):
  n = rabit[i]
  if i in skip:
    continue
  if rabit[n-1] == i+1:
    skip.add(n-1)
    num += 1
 
print(num)