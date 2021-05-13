X, A, B = list(map(int, input().split(' ')))
if B - A > X:
    print('dangerous')
elif B - A > 0:
    print('safe')
else:
    print('delicious')