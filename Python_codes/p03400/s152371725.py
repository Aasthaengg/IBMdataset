n = int(input())
d, x = map(int, input().split())
a = [int(input()) for i in range(n)]
c = 0
for i in range(n):
    for j in range(1, d + 1):
        if a[i] == 1:
            c += 1
        elif j % a[i] == 1:
            c += 1
print(c + x)