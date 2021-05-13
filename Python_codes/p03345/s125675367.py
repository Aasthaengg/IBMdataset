A, B, C, K = map(int, input().split())

if K % 2 == 0:
    if abs(A - B) >= int(1e18):
        print("Unfair")
    else:
        print(A - B)
else:
    if abs(A - B) >= int(1e18):
        print("Unfair")
    else:
        print(B - A)