#B - Minor Change
S = str(input())
T = str(input())
i = 0
j = 0
k = len(S)
for j in range(k):
    if S[j] != T[j]:
        i += 1
# 出力
print(i)