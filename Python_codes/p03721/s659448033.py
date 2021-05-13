n, k = map(int, input().split())
D = dict()
for i in range(n):
    a, b = map(int, input().split())
    if a in D.keys():
        D[a] += b
    else:
        D[a] = b

D = sorted(D.items(), key=lambda x: x[0])
for d in D:
    if k <= d[1]:
        print(d[0])
        break
    else:
        k -= d[1]