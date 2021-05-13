ais = sorted(map(int, raw_input().split()))
print 'Yes' if sum(ais[:2]) == ais[2] else 'No'