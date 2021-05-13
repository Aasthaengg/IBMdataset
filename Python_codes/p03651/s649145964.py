n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)

h = a[0]
gcda = a[0]

for i in range(1, n):
    if a[i] > h:
        h = a[i]

    gcda = gcd(gcda, a[i])

if k%gcda == 0 and k <= h:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")