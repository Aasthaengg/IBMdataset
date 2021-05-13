a = list(map(int, input().split()))
print("Yes" if abs(a[0]-a[2]) <= a[3] or abs(a[0]-a[1]) <= a[3] and abs(a[1]-a[2]) <= a[3] else "No")