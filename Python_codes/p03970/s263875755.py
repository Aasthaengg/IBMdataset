s = input()
t = "CODEFESTIVAL2016"

print(sum([i != j for i, j in zip(s, t)]))