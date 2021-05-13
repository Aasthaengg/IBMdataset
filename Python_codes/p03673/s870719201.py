n = int(input())
a = list(input().split())
result = list(reversed(a))[::2]

if n % 2 == 0:
    result += a[::2]
else:
    result += a[1::2]

print(*result)