n, m = map(int, input().split())
if 2 * n > m:
    print(m//2)
else:
    result = 0
    result += n
    m -= 2*n
    result += m//4
    print(result)