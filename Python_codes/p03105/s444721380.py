n = list(map(int, input().split()))
def ans(a, b, c):
    if a > b:
        return 0
    else:
        if int(b/a) < c:
            return int(b/a)
        else:
            return c
print(ans(n[0], n[1], n[2]))