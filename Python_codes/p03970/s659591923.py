S1 = str(input())
S2 = "CODEFESTIVAL2016"

cnt = 0
for i in range(len(S1)):
    if S1[i] != S2[i]:
        cnt += 1
print(cnt)