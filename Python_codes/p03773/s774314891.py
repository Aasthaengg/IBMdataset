a = list(map(int, input().split()))
b = a[0] + a[1]
print(b if b < 24 else b-24)