X = int(input())
if X > 2100:
    print('1')
else:
    if X <= 105*(X//100):
        print('1')
    else:
        print('0')