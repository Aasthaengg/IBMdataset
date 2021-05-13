X, Y, A, B, C = map(int, input().split())
p, q, r = [list(map(int, input().split())) for _ in range(3)]

p = sorted(p, reverse=True)[:X]
q = sorted(q, reverse=True)[:Y]

l = p+q+r

l.sort(reverse=True)

print(sum(l[:X+Y]))