l='#.'*151
while 1:
  h,w=map(int,raw_input().split())
  if h==0:break
  for i in range(h):
    if i%2:print l[1:w+1]
    else:print l[:w]
  print