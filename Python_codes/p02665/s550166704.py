N = int(input())
A = [int(i) for i in input().split()] 

total = sum(A)
node = 1
ans = 0
for i in range(N+1):
  ans += node
  total -= A[i]
  #print(node, total)
  node = min(total, (node - A[i]) * 2)
  
  if node < 0:
    print(-1)
    exit()
      
print(ans)