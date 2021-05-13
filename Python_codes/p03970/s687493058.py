S = input()
cor = "CODEFESTIVAL2016"
count = 0
for i in range(len(S)):
    if S[i] != cor[i]:
        count += 1
print(count)
