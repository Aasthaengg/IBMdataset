N=int(input())
v=list(map(int,input().split()))

v.sort()
for i in range(N-1):
  A=(v[0]+v[1])/2
  del v[0]
  del v[0]
  v.insert(0,A)
  
print(v[0])
