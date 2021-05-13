S = list(input())
V = list(reversed(S))

cnt = 0
for i in range(int(len(S)/2)):
    if S[i] != V[i]:
        cnt += 1
print(cnt)