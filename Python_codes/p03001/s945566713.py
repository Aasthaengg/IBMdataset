w,h,x,y = map(int, input().split())
a = []
a.append(w*h/2)
if x*2==w and y*2==h:
  a.append(1)
else:
  a.append(0)
print(' '.join(map(str,a)))