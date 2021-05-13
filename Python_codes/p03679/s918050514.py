X, A, B = map(int,input().split())
if A - B + X < 0:
    print('dangerous')
elif A - B < 0:
    print('safe')
else:
    print('delicious')