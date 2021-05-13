N  = int(input())
rs = [ [ *input().split(), n ] for n in range(N) ]

rs = sorted(
    [ (f'{s}{100 - int(p):03}', i + 1) for s, p, i in rs ],
    key=lambda t: t[0],
)

for r in rs:
    print(r[1])