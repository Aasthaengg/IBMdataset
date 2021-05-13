def abc154c_distinct_or_not():
    n = int(input())
    a = set(map(int, input().split()))
    if n == len(a):
        print('YES')
    else:
        print('NO')

abc154c_distinct_or_not()