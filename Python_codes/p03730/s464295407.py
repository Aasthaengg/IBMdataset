a, b, c = (int(x) for x in input().split())
print("YES" if c in [a * (x + 1) % b for x in range(b)] else "NO")