S = str(input())
T = str(input())
lenS = len(S)
lenT = len(T)
max_match = 0
for idx in range(lenS - lenT + 1):
    cnt_match = 0
    for i in range(lenT):
        if S[idx + i] == T[i]:
            cnt_match += 1
    if cnt_match > max_match:
        max_match = cnt_match
print(lenT - max_match)

