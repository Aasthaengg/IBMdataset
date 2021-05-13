A, B, C = map(int, input().split())
if 0 in (A % 2, B % 2, C % 2):
    print(0)
else:
    print(min(A * B, B * C, C * A))
