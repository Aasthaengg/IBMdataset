X = input().split()
x = int(X[0])
if x < 1200:
    print('ABC')
elif 1200 <= x < 2800:
    print('ARC')
else:
    print('AGC')