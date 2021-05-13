from itertools import accumulate
def prime(n):
  if n==1:
    return False
  else:
    for i in range(2,int(n**0.5)+1):
      if n%i==0:
        return False
    else:
      return True

l = [0 for i in range(10**6)] 

for i in range(1,10**5+1):
  if i%2==0:
    continue
  else:
    if prime(i):
      if prime((i+1)//2):
        l[i] = 1
l1 = list(accumulate(l))
q = int(input())
for i in range(q):
  l,r = map(int,input().split())
  print(l1[r]-l1[l-1])