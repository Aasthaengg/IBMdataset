# B - Making Triangle

n = int(input())
l = list(map(int, input().split()))
assert n == len(l)

count = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if l[i] == l[j] or l[j] == l[k] or l[k] == l[i]:
                continue
            a, b, c = sorted((l[i], l[j], l[k]))
            if a + b > c:
                count += 1
print(count)
