n, m, x, *aa = map(int, open(0).read().split())

print(min(len([a for a in aa if a<x]), len([a for a in aa if a>x])))