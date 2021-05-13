n, x = map(int, input().split())
m = [int(input()) for i in range(n)]
ret = n
x -= sum(m)
y = min(m)
ret += x//y
print(ret)