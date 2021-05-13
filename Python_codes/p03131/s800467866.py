k, a, b = map(int, input().split())

if b - a <= 2:
    print(k + 1)
else:
    k = k - (a - 1)
    cnt = a

    ab = k // 2
    cnt += (b - a) * ab + k % 2
    print(cnt)