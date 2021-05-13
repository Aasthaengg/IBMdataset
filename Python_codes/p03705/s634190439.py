def answer(n, a, b):
    if (a > b): return 0
    if n == 1 and a != b: return 0
    n = n-2
    small = a*n
    big = b*n
    return big - small + 1

n, a, b = map(int, input().split())
print(answer(n, a, b))