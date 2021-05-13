S = input().strip()
K = int(input())

ans = ""
for i, s in enumerate(S):
    if i == len(S) - 1:
        if ord(s) + K <= ord("z"):
            ans += chr(ord(s) + K)
        else:
            ans += chr(ord("a") + (ord(s) + K - ord("z") - 1) % 26)
    elif s == "a":
        ans += "a"
        continue
    elif ord("z") + 1 - ord(s) <= K:
        ans += "a"
        K -= (ord("z") + 1 - ord(s))
    else:
        ans += s

print(ans)

