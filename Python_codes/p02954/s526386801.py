S = input()

cnt = 1
loc = {}
for i in range(len(S)-1):
    if S[i] == "R" and S[i + 1] == "L":
        if i%2 == 0:
            loc[cnt] = [i, i+1]
        else:
            loc[cnt] = [i+1, i]
        cnt += 1

cnt = 1
p = []
for i in range(len(S)-1):
    p.append(cnt)
    if S[i] == "L" and S[i+1] == "R":
        cnt += 1
p.append(cnt)

ans = [0] * len(p)
for i in range(0, len(S), 2):
    ans[loc[p[i]][0]] += 1

for i in range(1, len(S), 2):
    ans[loc[p[i]][1]] += 1

print(" ".join(map(str, ans)))