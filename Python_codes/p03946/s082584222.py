n, t = map(int, input().split())
l = [int(i)for i in input().split()]

if t <= 1 or all(a >= b for a, b in zip(l, l[1:])):
    print(0)
else:
    mini = float("inf")
    maxp = 0
    maxc = 0
    for n in l:
        if n - mini > maxp:
            maxp = n - mini
            maxc = 1
        elif n - mini == maxp:
            maxp = n - mini
            maxc += 1
        mini = min(mini, n)
    print(maxc)