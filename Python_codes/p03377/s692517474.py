A, B, X = list(map(int, input().split()))
if X - A <= B and X >= A:
    print("YES")
else:
    print("NO")
