n = int(input())
SP = []
for i in range(n):
    s, p = map(str, input().split())
    p = int(p)
    SP.append((s, p, i+1))
SP.sort(key=lambda x: (x[0], -x[1]))
for s, p, j in SP:
    print(j)
