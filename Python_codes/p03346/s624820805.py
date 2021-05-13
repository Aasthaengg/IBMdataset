N = int(input())
P = [int(input()) for _ in range(N)]

d = {}
for i in P:
    if i-1 in d.keys():
        d[i] = d[i-1] + 1
    else:
        d[i] = 1

print(N-max(d.values()))
