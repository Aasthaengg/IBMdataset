S = input()
T = input()
LS = len(S)
LT = len(T)

ans = LT

for i in range(0, LS-LT+1):
    cnt = 0
    for j in range(0, LT):
        if S[i+j] != T[j]:
            cnt += 1
    ans = min(ans, cnt)

print(ans)
