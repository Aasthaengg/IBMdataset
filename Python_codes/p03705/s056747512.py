N, A, B = map(int, input().split())
diff = B - A

if N == 1:
    if diff != 0:
        print(0)
    else:
        print(1)
else:
    if diff < 0:
        print(0)
    elif diff == 0:
        print(1)
    else:
        max_val = B * (N-1) + A
        min_val = A * (N-1) + B
        print(max_val - min_val + 1)
