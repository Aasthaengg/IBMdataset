INPUT = list(map(int,input().split()))
x=INPUT[0]
a=INPUT[1]
b=INPUT[2]
if abs(x-a)>abs(x-b):
    print('B')
else:
    print('A')
