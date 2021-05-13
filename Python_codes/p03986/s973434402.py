X = input()
N = len(X)

cnt_s = 0
ans = N
for i in range(N):
    if X[i] == "S":
        cnt_s += 1
    else:
        if cnt_s > 0:
            ans -= 2
            cnt_s -= 1

print(ans)
