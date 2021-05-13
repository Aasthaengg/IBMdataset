N,A,B = map(int, input().split())
if A % 2 == B % 2:
    print((B-A) // 2)
else:
    x = min(B - 1, N - A)
    y = 1 + min(A - 1, N - B) + (B - A) // 2
    print(min(x, y))
