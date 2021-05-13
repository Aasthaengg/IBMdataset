A,B=map(int,input().split())
if A%3*B%3*(A+B)%3==0:print('Possible')
else:print('Impossible')