n = int(input())
a = int(input())
n -= (n//500) * 500
print('Yes' if a >= n else 'No')
