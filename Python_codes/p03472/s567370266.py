N, H = map(int, input().split())

A = []
B = []

for _ in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)
  

def solve():
  count = 0
  remain = H
  
  B.sort()
  
  max_a = max(A)
  
  while B:
    if remain <= 0:
      return count
    
    b = B.pop()
    
    if b < max_a:
      break
      
    remain -= b
    count += 1
  
  count += (remain + max_a - 1) // max_a
    
  return count

print(solve())