n, m = map(int, input().split())

if n < 1 or m < 2:
    print(0)
    quit()

if n <= m:
    if 2*n == m:
        print(n)
    elif 2*n < m:
        print(n + (m-2*n)//4)
    elif 2*n > m:
        print(m//2)
else:
    print(m//2)
