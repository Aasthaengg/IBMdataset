S = list(input())

ans = 0
cnt = 0
i = len(S)-1
while i >= 0:
    if i > 0 and S[i] == "C" and S[i-1] == "B":
        cnt += 1
        i -= 2
    elif S[i] == "A":
        ans += cnt
        i -= 1
    else:
        cnt = 0
        i -= 1
print(ans)