n = int(input())
d, x = map(int, input().split())

s = x
for _ in range(n):
    a = int(input())
    k = 0
    while k*a <= d-1:
        s += 1
        k += 1
print(s)
