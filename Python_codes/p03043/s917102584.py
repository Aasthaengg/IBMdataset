N,K = map(int, input().split())
a = 0
for i in range(1,N+1):
  c = 0
  while i<K:
    c+=1
    i*=2
  a += (0.5**c)/N
 
print(a)