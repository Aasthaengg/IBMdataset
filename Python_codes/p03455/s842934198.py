# 二つの正整数 a,b aとbの積が偶数か奇数か

a,b = map(int,input().split())

if (a * b ) % 2 == 0:
    print('Even')

if (a * b) % 2 != 0:
    print('Odd')