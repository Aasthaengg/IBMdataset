seta = set([1,3,5,7,8,10,12])
setb = set([4,6,9,11])
setc = set([2])
 
a,b = map(int, input().split())
 
if (a in seta and b in seta) or (a in setb and b in setb) or (a in setc and b in setc):
  print('Yes')
else:
  print('No')