a, b, c = map(int, input().split())
L = sorted([a, b, c])
print("Yes" if L[0] + L[1] == L[2] else "No")