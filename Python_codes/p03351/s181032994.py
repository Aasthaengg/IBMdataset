a, b, c, d = list(map(int, input().split()))
print("YNeos"[abs(a - c) > d and any((abs(b - c) > d, abs(a - b) > d))::2])