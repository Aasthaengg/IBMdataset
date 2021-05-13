a = list(map(int,input().split()))
A = a[0]
B = a[1]

if (A+B)%3==0 or A%3==0 or B%3==0:
    print('Possible')
else:
    print('Impossible')
