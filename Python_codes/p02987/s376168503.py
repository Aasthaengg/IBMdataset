s = input()
a = sorted(s)
print("Yes" if a[0]==a[1] and a[2]==a[3] and a[0] != a[2] else "No")
