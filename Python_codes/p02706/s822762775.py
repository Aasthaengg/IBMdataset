n = input()
n = n.split()
m = int(n[1])
n = int(n[0])
a = input()
a = a.split()
b = int(a[0])
for c in range(m-1):
    b = b + int(a[c+1])
if n - b < 0:
    print("-1")
else:
    print(n-b)