N = int(input())
li = [0]*101

for _ in range(N):
  D = int(input())
  li[D] = 1
  
print(sum(li))