A, B, C, K = map(int,input().split())

if K % 2 == 1:
    ans = B - A
else:
    ans = A - B

if abs(ans) > 10 ** 18:
    print("Unfair")
else:
    print(ans)