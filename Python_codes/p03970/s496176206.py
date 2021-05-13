S = input().strip()
X = "CODEFESTIVAL2016"
cnt = 0
for i in range(len(S)):
    if S[i]!=X[i]:
        cnt += 1
print(cnt)