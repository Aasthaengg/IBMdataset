n, aa = [list(map(lambda x:int(x), s.split())) for s in open(0)]

print(sum(a-1 for a in aa))