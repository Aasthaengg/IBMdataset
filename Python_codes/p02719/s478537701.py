n, k = map(int , input().split())

if n%k > abs(n%k-k):  
  print(abs(n%k-k))
else :
  print(n%k)