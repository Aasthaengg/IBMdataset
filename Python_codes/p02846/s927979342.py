a,b,c,d,e,f=map(int,open(0).read().split());g,h=(c-e)*a,(d-f)*b
if g>0:g,h=-g,-h
i=g+h
if i<0:print(0)
elif i==0:print("infinity")
else:print(2*(-g//i)+[0,1][int(bool(-g%i))])