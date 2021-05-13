A1, A2, A3 = map(int, input().split())

num = A1+A2+A3

if 22<=num:
    print('bust')

elif num<=21:
    print('win')