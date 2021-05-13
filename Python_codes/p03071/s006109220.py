A, B = map(int, input().split())
large = max(A, B)
if A == B:
    print(large + large)
else:
    print(large + (large-1))