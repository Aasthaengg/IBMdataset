S = input()

truth = "CODEFESTIVAL2016"

c = 0
for i in range(len(S)) :
    if (S[i] != truth[i]) :
        c += 1

print(c)