n = int(input())
ans = 100000
for i in range(1, n):
    a, b = str(i), str(n-i)
    A, B = 0, 0
    for x in a:
        A += int(x)
    for y in b:
        B += int(y)
    ans = min(ans, A+B)
print(ans)