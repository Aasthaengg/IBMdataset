A, B, C, K = map(int, input().split())

ans = A - B
if abs(ans) <= 10 ** 18:
    if K % 2 == 0:
        print(ans)
    else:
        print(ans * -1)
else:
    print("Unfair")