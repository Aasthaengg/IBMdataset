import math
N, A, B = map(int, input().split())
h = [int(input()) for _ in range(N)]

h.sort(reverse = True)

def det(m):
  C = [max(0, a-B*m) for a in h]
  #print(m, C)
  if sum([math.ceil(b/(A-B)) for b in C]) > m:
    return False
  else:
    return True
  
l = 0
r = math.ceil(max(h)/A*N)
#print(l, r)
while r - l > 1:
  c = (l + r) // 2
  if det(c):
    r = c
  else:
    l = c
    
print(r)
    
  
  
