a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
mi = min(a, b, c, d, e)
ma = max(a, b, c, d, e)
if ma - mi > k:
    print(":(")
else:
    print("Yay!")
