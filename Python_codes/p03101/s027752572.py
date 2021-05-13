a = list(map(int, input().split()))
b = list(map(int, input().split()))
H = a[0]
W = a[1]
h = b[0]
w = b[1]
k = (H - h) * (W - w)
print(k)
