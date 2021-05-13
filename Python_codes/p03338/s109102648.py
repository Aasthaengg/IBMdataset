N = int(input())
S = input()

ans = 0
for i in range(1, len(S)):
    tmp = 0
    X = set(S[:i])
    Y = set(S[i:])
    for x in X:
        if x in Y:
            tmp += 1
    ans = max(ans, tmp)
print(ans)