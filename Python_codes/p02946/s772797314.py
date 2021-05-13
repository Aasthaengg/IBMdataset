k, x = map(int, input().split())
a = [x]

for i in range(1, k):
    a.append(x - i)
    a.append(x + i)
a.sort()
print(*a)