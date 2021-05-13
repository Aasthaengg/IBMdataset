S = input()

count = 0
for s, t in zip(S, "CODEFESTIVAL2016"):
    if s != t:
        count += 1

print(count)