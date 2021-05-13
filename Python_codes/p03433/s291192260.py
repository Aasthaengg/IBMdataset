n = int(input())
a = int(input())
ans = n - (n // 500) * 500
if ans > a:
    print('No')
else:
    print('Yes')
