a = sorted(map(int, input().split()))
print("Yes" if (a[0] == a[1] or a[1] == a[2] ) and a[0] != a[2] else "No")