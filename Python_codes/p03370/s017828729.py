n, x = map(int, input().split())
d = [int(input()) for i in range(n)]
da = sum(d)
print((x-da)//min(d) + n)