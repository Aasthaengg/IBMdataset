S = input()
correct = "CODEFESTIVAL2016"
count = 0
for i in range(16):
    if S[i] != correct[i]:
            count += 1
print(count)