
n, m = map(int, input().split())
if m == 1:
    print(1, n)
    exit()
if n % 2 == 1:
    for i in range(m):
        print(i+1, n-i-1)
else:
    j = 1
    for i in range((m-1)//2+1):
        print(j, n - i)
        j += 1
    j += 1
    for i in range((m-1) // 2+1, m):
        print(j, n - i)
        j += 1
