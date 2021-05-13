n, x = map(int, input().split())
a = list(map(int, input().split()))
result = 0
if a[0] > x:
    result += (a[0] - x)
    a[0] = x
for i in range(1, n):
    box2 = a[i-1] + a[i]
    if x < box2:
        result += box2 - x
        a[i] -= box2 - x
print(result)