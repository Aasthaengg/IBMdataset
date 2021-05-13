n, k = [ int(i) for i in input().split(' ') ]
xs = [ int(x) for x in input().split(' ') ]
i0 = xs.index(min(xs))
print(1 + min([ (i + k - 2) // (k - 1) + (n - i - 2) // (k - 1)
  for i in range(max(i0 - k + 1, 0), min(i0, n - k) + 1) ]))