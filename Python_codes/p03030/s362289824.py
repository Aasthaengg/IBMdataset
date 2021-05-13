_, *sp = open(0).read().split()
for _, _, a in sorted([(s, -int(p), i + 1) for i, (s, p) in enumerate(zip(*[iter(sp)] * 2))]):
    print(a)