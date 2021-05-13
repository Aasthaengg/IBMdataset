a = [int(input()) for _ in range(4)]
print(min(a[0], a[1])*a[2]+max(0, (a[0]-a[1])*a[3]))
