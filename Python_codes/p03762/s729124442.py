n,m = map(int, input().split())
X = [int(x) for x in input().split()]
Y = [int(x) for x in input().split()]
def f(a, n):
    return sum([(n - 1 - 2*i) * x for i, x in enumerate(reversed(a))])
print(f(X, n) * f(Y, m) % (10**9 + 7))