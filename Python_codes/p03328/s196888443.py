def main():
    a, b = map(int, input().split())
    t = 0
    r = -10**9
    for i in range(1, 1000):
        t += i
        if t <= i:
            continue
        if r == t - b:
            return r
        r = t - a

print(main())
