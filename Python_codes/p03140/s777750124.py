from sys import stdin
import fractions

n = int(stdin.readline().rstrip())
a = stdin.readline().rstrip()
b = stdin.readline().rstrip()
c = stdin.readline().rstrip()

point = 0
for i in range(n):
    if a[i] != b[i] and b[i] == c[i]:
        point += 1
    elif a[i] == b[i] and b[i] != c[i]:
        point += 1
    elif a[i] == c[i] and b[i] != a[i]:
        point += 1
    elif a[i] != c[i] and b[i] != a[i]:
        point += 2

print(point)