s = input()
n, k = [int(i) for i in s.split(' ')]

if (n + 1) / 2 >= k:
    print('YES')
else:
    print('NO')
