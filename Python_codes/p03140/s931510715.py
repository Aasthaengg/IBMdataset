n = int(input())
a = input()
b = input()
c = input()
p = 0

for i in range(n):
    if a[i] == b[i] == c[i]:
        pass
    else:
        if a[i] == b[i]:
            p += 1
        elif b[i] == c[i]:
            p += 1
        elif a[i] == c[i]:
            p += 1
        else:
            p += 2

print(p)