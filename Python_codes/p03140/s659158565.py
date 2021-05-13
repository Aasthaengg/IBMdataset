n = int(input())

a = list(input())
b = list(input())
c = list(input())

count = 0

for i in range(n):
    if a[i] != b[i] and b[i] != c[i] and c[i] != a[i]:
        count += 2
    elif a[i] == b[i] and b[i] == c[i]:
        continue
    else:
        count += 1

print(count)

