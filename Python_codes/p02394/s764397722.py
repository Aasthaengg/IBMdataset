def hantei(W,H,x,y,r):
 if x-r < 0:
  return 'No'
 if x+r > W:
  return 'No'
 if y-r < 0:
  return 'No'
 if y+r > H:
  return 'No'
 else:
  return 'Yes'

W,H,x,y,r = map(int,raw_input().split())
print hantei(W,H,x,y,r)