n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
b = 0
for i in range(n):
    b = a[b] - 1
    if b == 1:
        print(i + 1)
        exit()
print(-1)