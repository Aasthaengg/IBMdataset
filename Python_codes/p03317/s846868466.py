n,k = map(int,input().split())
count = 1
n = n-k

while 0<n:
  n = (n+1) - k
  count = count + 1
  
print(count)