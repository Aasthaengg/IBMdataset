(n, m, c), bb, *aaa = [list(map(int, l.split())) for l in open(0)]

ans = 0

print(sum((sum(b*a for b, a in zip(bb, aa))+c>0) for aa in aaa))