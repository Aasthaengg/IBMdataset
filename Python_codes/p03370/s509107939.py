n, x = map(int, input().split())
m = [int(input()) for i in range(n)]
a = sum(m)
c = n
while a + min(m) <= x:
    a += min(m)
    c += 1
print(c)