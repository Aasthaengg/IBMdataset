A, B = map(int, input().split())
if A != B:
    x = max(A, B)
    print(2*x-1)
else:
    print(A + B)