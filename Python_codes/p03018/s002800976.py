S = "???" + input() + "???"

a = 0

ans = 0
i = 0
while i < len(S):
    s = S[i]

    if s == "A":
        a += 1
        i += 1
        while i < len(S):
            s1 = S[i]
            s2 = S[i + 1]

            if s1 == "A":
                a += 1
                i += 1
                continue
            elif s1 + s2 == "BC":
                ans += a
                i += 2
            else:
                break

        a = 0
    else:
        i += 1
        continue

print(ans)
