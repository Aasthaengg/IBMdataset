X = int(input())
  
# 順に素数判定を行えばよい
def is_prime(x):
  if x <= 1:
    return False
  for i in range(2, x):
    if x % i == 0:
      return False
  return True
 
p = X
while not is_prime(p):
  p += 1
  
print(p)