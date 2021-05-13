l, r, d = map(int, input().split())

def count(x):
    return x // d

print(count(r) - count(l-1))