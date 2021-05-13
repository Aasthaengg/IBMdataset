N = int(input())

d = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}

for i in range(N):
    a = input()
    d[a] += 1

for x, y in d.items():
    print("{0} x {1}".format(x, y))
