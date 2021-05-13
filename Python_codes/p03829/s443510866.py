N,A,B = [ int(it) for it in input().split() ]
li = [ int(it) for it in input().split() ]
s = 0
for i in range(len(li)-1):
  d = li[i+1] - li[i]
  if (A*d<B):
    ds = d*A
  else:
    ds = B
  s+=ds
print (s)
    
  

