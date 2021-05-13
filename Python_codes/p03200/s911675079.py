S = input()
N = len(S)

ans = 0
bnum = 0

for i in range(N):
    if S[i] == "B":
        bnum += 1
    else:
        ans += bnum

print(ans)