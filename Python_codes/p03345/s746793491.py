A, B, C, K = map(int, input().split())

sub = 0
limit = 10**18
if K % 2 == 0:
    sub = A - B
else:
    sub = B - A
if abs(sub) > limit:
    print("Unfair")
else:
    print(sub)
