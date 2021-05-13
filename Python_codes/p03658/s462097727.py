n,k = map(int, raw_input().split())
ais = map(int, raw_input().split())
ais.sort()
print sum(ais[-k:] or [0])