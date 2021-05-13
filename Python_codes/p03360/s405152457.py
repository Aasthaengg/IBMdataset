def f(a, b, c, k):
    abc = sorted([a, b, c])
    if k != 0:
        abc[2] *= 2 ** k
    print(sum(abc))

a, b, c = map(int, input().split())
k = int(input())
f(a, b, c, k)
