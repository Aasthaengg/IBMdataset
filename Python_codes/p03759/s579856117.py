(a, b, c) = (int(tok) for tok in input().split())
print("YES" if (b - a == c - b) else "NO")
