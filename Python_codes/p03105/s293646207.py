A, B, C = map(int, input().split())
print(C if C * A <= B else B // A)
