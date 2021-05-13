a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
s = list(sorted([a, b, c, d, e]))
d_min = s[0]
d_max = s[-1]
if d_max - d_min > k:
    print(":(")
else:
    print("Yay!")
