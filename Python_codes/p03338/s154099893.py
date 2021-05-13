N = int(input())
S = input()
cnt = 0
alpha = []
ans = []

for i in range(1, N):
    alpha = []
    cnt = 0
    X = S[:i]
    Y = S[i:]
    for j in X:
        if j in alpha: continue
        if Y.count(j) > 0:
            cnt += 1
            alpha.append(j)

    ans.append(cnt)

print(max(ans))