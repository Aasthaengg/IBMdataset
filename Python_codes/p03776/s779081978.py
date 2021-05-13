from math import factorial


def comb(a, b):
    if b < 0 or a < b:
        return 0
    return factorial(a) // factorial(b) // factorial(a - b)


N, A, B = map(int, input().split())
V = [int(s) for s in input().split()]
V.sort(reverse=True)
ans1 = sum(V[:A]) / A
num = V.count(V[A - 1])
if V[0] == V[A - 1]:
    ans2 = sum([comb(num, m) for m in range(A, B + 1)])
else:
    m = V[:A].count(V[A - 1])
    ans2 = comb(num, m)
print(ans1)
print(ans2)
