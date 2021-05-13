n, m = map(int, input().split())

if n % 2: # odd
    for i in range(m):
        print(i + 1, n - i)
else: # even
    for i in range(m):
        if 1 + 2 * i >= n - 1 - 2 * i:
            l1 = i
            break
        m -= 1
        print(i + 1, n - i)

    for i in range(m):
        if i + 1 + l1 >= n - i - l1 - 1:
            raise Exception()
        print(i + 1 + l1, n - i - l1 - 1)
