n, k = map(int, input().split())
l = list(map(int, input().split()))

l = list(sorted(l, reverse=True))
s = 0
for a in range(0, k):
    s += l[a]

print(s)
