r, D, xi = map(int, input().split())
base=xi
for i in range(1, 11):
    ret = r * base - D
    base = ret
    print(ret)
