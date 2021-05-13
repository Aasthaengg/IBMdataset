
S =  input()

ans = 0

prev,now = "",""

for i in range(len(S)):
    now += S[i]
    if now != prev:
        ans += 1
        prev,now = now,""

print(ans)
