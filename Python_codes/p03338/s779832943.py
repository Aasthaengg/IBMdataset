N = int(input())
S = input()

ans = 0
for i in range(1,N):
    X = list(set(S[:i]))
    Y = list(set(S[i:]))
    kaburi = 0
    for j in range(len(X)):
        for k in range(len(Y)):
            if X[j] == Y[k]:
                kaburi += 1
    if kaburi > ans:
        ans = kaburi

print(ans)