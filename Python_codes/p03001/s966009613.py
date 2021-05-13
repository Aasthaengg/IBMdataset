w,h,x,y=[int(x) for x in input().rstrip().split()]

dou=0
if w/2==x and h/2==y:
  dou=1

print(w*h/2,dou)