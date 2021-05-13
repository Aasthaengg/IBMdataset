n = int(input())
a = int(input())
if a >= 499:
    print('Yes')
elif n % 500 <= a:
    print('Yes')
else:
    print('No')