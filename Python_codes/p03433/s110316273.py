n = int(input())
a = int(input())
r = n % 500
if a < r:
    print('No')
else:
    print('Yes')