N, T, *_CT = map(int, open(0).read().split())
CT = list(zip(*[iter(_CT)]*2))

costs = [ct[0] for ct in CT if ct[1] <= T]
if costs == []:
    print("TLE")
else:
    print(min(costs))