n = int(input())
a = [2, 1]
for i in range(n):
    a.append(sum(a[-2:]))
print(a[n])