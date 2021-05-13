N = int(input())
d = [int(n) for n in input().split()]

d = sorted(d)

idx = int(N/2)

l = d[:idx][-1]
r = d[idx:][0]

print(r - l)