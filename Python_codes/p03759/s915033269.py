a = list(map(int, input().split()))
print("YES" if a[1] - a[0] == a[2] - a[1] else "NO")