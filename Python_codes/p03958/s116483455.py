n, k = map(int, input().split())
l = sorted(list(map(int, input().split())))
mx = l[-1]
s = sum(l[:-1])
print(max(0, mx-1-s))

