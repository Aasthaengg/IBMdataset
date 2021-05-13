l='#.'*999
c="\n"
while 1:
 h,w=map(int,raw_input().split())
 if h==0:break
 s=""
 for i in range(h):
  if i%2:s+=l[1:w+1]+c
  else:s+=l[:w]+c
 print s