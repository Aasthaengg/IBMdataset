A, B, C, K = map(int, input().split())

if K%2 == 0:
    if abs(A-B) <= 10**18:
        print(A-B)
    else:
        print("Unfair")
else:
    if abs(B-A) <= 10**18:
        print(B-A)
    else:
        print("Unfair")
