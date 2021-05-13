X, A, B = [int(i) for i in input().split()]

if B - A > X :
    print('dangerous')
elif B - A > 0 and B- A <= X:
    print('safe')
else :
    print('delicious')
