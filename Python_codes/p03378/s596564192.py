n, m, x = map(int, input().split())
a = list(map(int, input().split()))
b = 0
c = 0
for i in a:
    if i < x:
        b += 1
    else:
        c += 1
print(min(b, c))