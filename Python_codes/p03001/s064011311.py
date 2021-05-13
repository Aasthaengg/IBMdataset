w,h,x,y=map(int,input().split())

if w/2==x and h/2==y:
  print(str((h*w/2))+' '+str(1))
  
else:
  print(str((h*w/2))+' '+str(0))

