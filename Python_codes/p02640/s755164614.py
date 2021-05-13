X,Y=map(int,input().split())
if Y%2!=0:
    print('No')
elif Y/2<X or Y/4>X:
    print('No')
else:
    print('Yes')