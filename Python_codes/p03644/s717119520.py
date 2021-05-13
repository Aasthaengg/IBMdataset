N = int(input())
n = 0
while True:
  if 2**0 <= N <2**(n+1):
    break
  else:
    n +=1
print(2**n)