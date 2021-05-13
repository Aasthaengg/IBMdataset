a, s = map(int, input().split())
if a < 10:
    print(s + 100 * (10 - a))
else:
    print(s)