a, b, c, d = map(int, input().split())
ans_1 = abs(a - c) <= d
ans_2 = abs(a - b) <= d and abs(c - b) <= d
print("Yes" if ans_1 or ans_2 else "No")