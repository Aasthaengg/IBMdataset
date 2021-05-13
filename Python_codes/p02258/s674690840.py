n = input()
minv = input()
maxv = -2000000000 #10**9-10**9
for i in xrange(1, n):
    r = input()
    maxv = max(maxv, r - minv)
    minv = min(minv, r)

print maxv