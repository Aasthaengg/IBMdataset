A, B = list(map(int, input().split()))

if A >= 10 or B >= 10:
    print("-1")
else:
    ans = A * B
    print(ans)