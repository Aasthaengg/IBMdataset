A, P = map(int, input().split())

parts = 3 * A + P

if parts % 2 == 0:
    print(round(parts / 2))
else:
    print(round((parts - 1) / 2))