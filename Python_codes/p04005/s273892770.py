A, B, C = map(int, input().split())
def f(x, y, z):
    if x % 2 == 0:
        return 0
    else:
        return y * z
print(min(f(A, B, C), f(B, C, A), f(C, A, B)))
