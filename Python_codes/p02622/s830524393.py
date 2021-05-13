S, T = [list(input()) for _ in range(2)]
cnt = 0
for i in range(len(S)):
    if S[i] != T[i]:
        cnt += 1
print(cnt)
