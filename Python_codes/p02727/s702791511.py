x, y, a, b, c = map(int, input().split())
p = list(reversed(sorted(list(map(int, input().split())))))
q = list(reversed(sorted(list(map(int, input().split())))))
r = list(reversed(sorted(list(map(int, input().split())))))
del p[x:]
del q[y:]
l = list(reversed(sorted(p + q + r)))
print(sum(l[:x + y]))