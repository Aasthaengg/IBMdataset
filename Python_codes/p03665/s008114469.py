n, p = map(int, input().split())
A = list(map(int, input().split()))  

for a in A:
  if a % 2 != 0:
    break 
else:
  if p == 1: 
    print(0)
    exit()
  if p == 0: 
    print(2**n)
    exit()
  
ans = 2**(n-1)
print(ans)
