w,h,x,y=map(int,open(0).read().split())

if w==2*x and h==2*y:
    print('{} {}'.format(w*h/2,1))
else:
    print('{} {}'.format(w*h/2,0))