f = [1,3,5,7,8,10,12]
g = [4,6,9,11]
x,y = map(int,input().split())

if x == 2 and y == 2:
    print('Yes') 
elif x in f and y in f:
    print('Yes') 
elif x in g and y in g:
    print('Yes') 
else:
    print('No')    