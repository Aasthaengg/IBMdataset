S = input()
cands = ['Sunny', 'Cloudy', 'Rainy']
print(cands[(cands.index(S) + 1) % len(cands)])