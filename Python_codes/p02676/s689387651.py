k, s = open(0).read().split()
K = int(k)

if len(s) > K:
    print(s[:K] + "...")
else:
    print(s)
