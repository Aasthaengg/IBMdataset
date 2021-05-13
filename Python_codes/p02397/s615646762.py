for i in range(10000):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(min(a,b), max(a,b))
