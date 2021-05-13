H,W,N = [ int(it) for it in input().split() ]

di = set()

for i in range(N):
  di.add( tuple( int(it) for it in input().split() ) )

po = set()
for a,b in di:
  for da in [-1,0,1]:
    for db in [-1,0,1]:
      if (1<=a+da and a+da<=H and 1<=b+db and b+db<=W):
        po.add( (a+da,b+db) )

li = [0]*10
for a,b in po:
  k = 0
  if ( a == 1 or a == H or b == 1 or b == W ):
    continue
  for da in [-1,0,1]:
    for db in [-1,0,1]:
      if ( (a+da,b+db) in di ):
        k+=1
  li[k]+=1
li[0] += (H-2)*(W-2) - sum(li)      
      
for i in range(10):
  print ( li[i] )