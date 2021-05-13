N, A, B = map(int, input().split())

if abs(A - B) % 2 == 0:
    print((B - A) // 2)
else:
    left = B - 1
    right = N - A
    if abs(A - B) < 3:
        print(min(left, right))
    else:
        if left < right:
            print((B - A - 1) // 2 + A)
        else:
            print((B - A - 1) // 2 + N - B + 1)