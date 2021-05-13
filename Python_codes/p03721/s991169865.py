n, k = list(map(int, input().split()))
c = {}
cnts = []

for i in range(n):
    a, b = list(map(int, input().split()))
    if a in c:
        cnts[c[a]][1] += b
    else:
        c[a] = len(cnts)
        cnts.append([a, b])

cnts = sorted(cnts, reverse=True)

s = 0
while True:
    si = cnts.pop()
    s += si[1]

    if s >= k:
        print(si[0])
        break