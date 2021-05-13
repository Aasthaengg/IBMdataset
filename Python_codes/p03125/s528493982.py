A, B = map(int, input().split())

if not B % A:
    print(B + A)
else:
    print(B - A)