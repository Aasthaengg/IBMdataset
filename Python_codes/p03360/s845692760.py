a, b, c = map(int, input().split())
k = int(input())

for _ in range(k):
    if a > b and a > c:
        a *= 2
    elif b > a and b > c:
        b *= 2
    else:
        c *= 2
print(a + b + c) 