W,H,x,y,r = raw_input().split(' ')
W,H,x,y,r = int(W),int(H),int(x),int(y),int(r)
 
if x-r <0 or y-r <0 or x+r >W or y+r>H:
  print "No"
else:
  print "Yes"