S = input()
print("yes" if len(S)==len(set([s for s in S])) else "no")