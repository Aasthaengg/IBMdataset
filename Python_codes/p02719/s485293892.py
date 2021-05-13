n,k=list(map(int,input().split()))

# while k<n:
#   n-=k
if k<n:
  n-=n//k*k

# while k-n<n:
#   n=k-n
if k-n<n:
  n=k-n
  
print(n)