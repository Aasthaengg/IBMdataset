N, A, B = map(int, input().split())

if A == 0:
    print(0)
else:
    i = N // (A + B)
    j = N % (A + B)
    if j >= A:
        count = A * (i + 1)
        print(count)
    else:
        count = A * i + j
        print(count)