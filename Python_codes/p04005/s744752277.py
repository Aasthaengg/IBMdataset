x=list(map(int,input().split()))
x.sort()
if x[2]%2==0:
    print('0')
else:
    print(x[0]*x[1])