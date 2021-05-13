for _ in range(int(input())):
    a = [int(i) for i in input().split()]
    print('YES')  if a[0]**2 + a[1]**2 + a[2] ** 2 - max(a) **2 == max(a) ** 2 else print('NO')

