list = list(map(int,input().split()))

x=list[0]
a=list[1]
b=list[2]

if a>x:
    s=a-x
else:
    s=x-a

if b>x:
    t=b-x
else:
    t=x-b
    
if s<t:
    print('A')
else:
    print('B')