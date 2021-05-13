S = input()
correct = "CODEFESTIVAL2016"
rewrite = 0

for i in range(len(S)):
    if S[i] != correct[i]:
        rewrite += 1

print(rewrite)