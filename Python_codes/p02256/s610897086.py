def gc(x, y):
    while y > 0:
        x %= y
        x, y = y, x
    return x



A = [int(i) for i in input().split()]
print(gc(A[0],A[1]))
