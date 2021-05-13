N, A, B = map(int, input().split())
V = sorted([int(a) for a in input().split()])[::-1]

fa = [1]
for i in range(1, 60): fa.append(fa[-1] * i)
C = lambda a, b: fa[a] // (fa[a-b] * fa[b])

print(sum(V[:A])/A)
print(sum([C(V.count(V[i-1]), V[:i].count(V[i-1])) for i in range(A, B+1) if sum(V[:i])*A == sum(V[:A])*i]))