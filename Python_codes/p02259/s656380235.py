n = input()
a = map(int, raw_input().split())

c = 0
for i in range(n):
    for j in range(n - 1, i, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            c += 1

print(" ".join(map(str, a)))
print(c)