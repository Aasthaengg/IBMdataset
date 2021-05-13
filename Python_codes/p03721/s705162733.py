(N, K), *AB = [list(map(int, s.split())) for s in open(0)]
for a, b in sorted(AB):
    K -= b
    if K <= 0:
        print(a)
        break
