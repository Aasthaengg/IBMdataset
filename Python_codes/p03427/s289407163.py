def f(n):
    n = list(map(int, str(n)))
    if len(n) == 1:
        print(n[0])
    else:
        if sum([x - 9 for x in n]) != 0:
            mx = 9 * (len(n)-1) + n[0] - 1
        else:
            mx = 9 * len(n)
        print(max(mx, sum(n)))

n = int(input())
f(n)
