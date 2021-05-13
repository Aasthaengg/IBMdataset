N, K = map(int, input().split())
point = list(map(int, input().split())) #R, S, P
T = input()
te = ["r", "s", "p"]
past = []
ans = 0

for i,char in enumerate(T):
    index_win = (te.index(char) + 2) % 3
    te_win = te[index_win]
    if i >= K:
        if te_win == past[i - K]:
            past.append("$")
            continue
        else:
            ans += point[index_win]
    else:
        ans += point[index_win]
    past.append(te_win)

print(ans)
