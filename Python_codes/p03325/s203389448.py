n = int(input())
a = list(map(int, input().split()))

res = 0
for v in a:
    while v % 2 == 0:
        v //= 2
        res += 1

print(res)