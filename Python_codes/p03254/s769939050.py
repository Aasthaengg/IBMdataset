n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if sum(a) == x:
    print(n)
    exit()
if sum(a) < x:
    print(n-1)
    exit()
i = n
while sum(a[:i]) > x:
    i -= 1
print(i)