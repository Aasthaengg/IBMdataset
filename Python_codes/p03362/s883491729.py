import sys
input = sys.stdin.readline
def isprime(n):
  if n <= 1:
    return False
  else:
    for i in range(2,int((n)**0.5+1)):
      if n%i == 0:
        return False
    return True

def solve():  
  n = int(input())
  query = []
  for i in range(2,55555):
    if isprime(i):
      if i%5 == 1:
        query.append(i)
  print(*query[0:n])
    
solve()