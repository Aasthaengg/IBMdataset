price = int(input())
num1 = int(input())

amari = price % 500

if amari <= num1:
    print('Yes')
else:
    print('No')