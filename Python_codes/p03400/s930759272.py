n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]

res = x
for v in a:
    res += (d - 1) // v + 1
print(res)