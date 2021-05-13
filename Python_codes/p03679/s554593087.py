X,A,B=map(int,input().split())
Expired=B-A

if Expired<=0:
    print('delicious')
elif 0<Expired<=X:
    print('safe')
else:
    print('dangerous')