N, K = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
arr.sort()
mem = [False for i in range(K+1)]
mem[0] = False
for i in range(K):
  local_result = mem[i]
  for j in arr:
    if i+j <= K:
      mem[i+j] =  mem[i+j] or not local_result
mem[0] = True
#print(mem)
if mem[K]:
  print("First") 
else:
  print("Second")