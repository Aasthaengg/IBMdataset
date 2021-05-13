def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

k = int(input())
sum = 0
for a in range(k):
    for b in range(k):
        gcd_ab = gcd(a + 1, b + 1)
        for c in range(k):
            sum += gcd(gcd_ab, c + 1)
print(sum)