w,h,x,y=map(int,input().split())
if (x,y)==(w/2,h/2):
  frag=1
else:frag=0
print(w*h/2,frag)