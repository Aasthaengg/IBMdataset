input()
p = list(map(int, input().split()))
print(sum(pi < pj < pk or pk < pj < pi for pi, pj, pk in zip(p, p[1:], p[2:])))
