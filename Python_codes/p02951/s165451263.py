a, b, c = list(map(int, input().rstrip().split()))
r = c - (a -b)
r = max(r, 0)
print(r)