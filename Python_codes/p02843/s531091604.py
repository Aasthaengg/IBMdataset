X = int(input())

mod = X % 100
syou = X // 100

if (mod <= syou * 5):
    print('1')
else:
    print('0')
