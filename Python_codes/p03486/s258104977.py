s, t = [input() for _ in range(2)]

smin = "".join(sorted([c for c in s]))
tmax = "".join(reversed(sorted([c for c in t])))

print('Yes' if smin < tmax else 'No')
