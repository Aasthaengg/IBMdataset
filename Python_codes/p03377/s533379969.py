A, B, X = map(int, input().split())

if B >= X - A and X - A >= 0:
    print("YES")
else:
    print("NO")