S = input()
correct = "CODEFESTIVAL2016"
cnt = 0
for i in range(len(S)):
    if S[i] == correct[i]:
        cnt += 1

print(len(S) - cnt)