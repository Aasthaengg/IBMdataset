p=0
n,k=map(int, input().split())
for i in range(1, n+1):
  q=1/n
  j=0
  while i*2**j<k:
    j=j+1
    q=q/2
  p=p+q
print(p)