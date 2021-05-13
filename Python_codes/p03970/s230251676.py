s = input()
t = "CODEFESTIVAL2016"

print(sum([c1 != c2 for (c1, c2) in zip(s, t)]))