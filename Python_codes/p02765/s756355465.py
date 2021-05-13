# ABC156A

def f(n, r):
    if n >= 10:
        print(r)
    else:
        print(r + 100 * (10 - n))

n, r = map(int, input().split())
f(n, r)
