n = int(input())
a = int(input())

n = n % 500

if n % 500 == 0:
    print('Yes')
else:
    n = n % 500
    if (n <= a):
        print('Yes')
    else:
        print('No')

