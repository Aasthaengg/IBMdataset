import math

X,A,B=list(map(int, input().split()))

if A>=B:
    print('delicious')
elif B-A>X:
    print('dangerous')
else:
    print('safe')