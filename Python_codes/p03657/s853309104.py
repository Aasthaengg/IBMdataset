A,B=map(int,input().split());s='ossible'
if A%3*B%3*(A+B)%3==0:print('P'+s)
else:print('Imp'+s)