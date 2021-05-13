a, b, c = map(int, input().split())
K = int(input())

for i in range(K):
    if (a == max(a, b, c)):
        a *= 2
    elif (b == max(a, b, c)):
        b *= 2
    else:
        c *= 2

print(a + b + c)
