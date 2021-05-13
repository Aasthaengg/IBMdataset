x, n = map(int, input().split())
p = [int(i) for i in input().split()]
if n == 0:
    print(x)
else:
    under = over = x
    for num in range(x - min(p) + 2):
        if not (x - num in p):
            under = x - num
            break
    for num in range(max(p) - x + 2):
        if not (x + num in p):
            over = x + num
            break
    if x - under <= over - x:
        print(under)
    else:
        print(over)    