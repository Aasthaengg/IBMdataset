N = int(input())
def is_prime(x):
  if x<=1:return False
  for i in range(2,x):
    if x%i==0 : return False
  return True

while not is_prime(N):N+=1
print(N)