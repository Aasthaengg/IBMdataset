n = int(input())
a = str(input())
b = str(input())
c = str(input())
d = 0
for i in range(n):
    if a[i] == b[i] == c[i]:
        pass
    elif a[i] != b[i] and b[i] != c[i] and c[i] != a[i]:
        d += 2
    else:
        d += 1
print(d)