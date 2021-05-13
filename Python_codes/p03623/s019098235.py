x,a,b=map(int,input().split())

a_=abs(x-a)
b_=abs(x-b)
if a_>b_:
    print('B')
else:
    print('A')    
