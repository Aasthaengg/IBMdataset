N, *SP = open(0).read().split()
sp = sorted((s, -int(p), i) for i, (s, p) in enumerate(zip(*[iter(SP)] * 2), 1))
[print(i) for _, _, i in sp]
