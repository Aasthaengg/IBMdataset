n = int(input())
a = list(input())
b = list(input())
c = list(input())
counter = 0
for i in range(n):
    if a[i] == b[i] == c[i]:
        counter += 0
    elif a[i] == b[i] or b[i] == c[i] or a[i] == c[i]:
        counter += 1
    else:
        counter += 2
print(counter)