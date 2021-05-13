x, y, a, b, c = map(int,input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)

pqr = p[:x] + q[:y] + r
pqr.sort(reverse=True)
print(sum(pqr[:x+y]))