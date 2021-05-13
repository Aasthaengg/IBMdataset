n, k = map(int, input().split())

if n // k <= 0:
    print(0)
elif k == 1:
    print(0)
else:
    max_num = n - k + 1
    print(max_num - 1)