N, K = map(int, input().split())
H = [int(x) for x in input().split()]
Ha = sorted(H, reverse=True)
del Ha[:K]
print(sum(Ha))
