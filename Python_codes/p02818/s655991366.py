a, b, k, = map(int, input().split())

if a > 0 and k > 0:
    eat = a
    if a > k:
        eat = k
    a -= eat
    k -= eat

if b > 0 and k > 0:
    eat = b
    if b > k:
        eat = k
    b -= eat
    k -= eat

print("{} {}".format(a, b))