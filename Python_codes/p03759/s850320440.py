a, b, c = (int(i) for i in input().split())
print("YES" if b-a == c-b else "NO")