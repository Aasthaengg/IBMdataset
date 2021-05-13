n, x = map(int, input().split())
m = [int(input()) for i in range(n)]

x -= sum(m)
res = x//min(m)

print(n+res)