S = input()

ans = len(S)
s = 0
for i in range(ans):
    if S[i] == "S":
        s += 1
    else:
        if s > 0:
            s -= 1
            ans -= 2

print(ans)