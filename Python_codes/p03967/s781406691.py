s = list(input())
g_minus_p = 0
score = 0
for i in range(len(s)):
    if g_minus_p > 0:
        g_minus_p -= 1
        if s[i] == "g":
            score += 1
    else:
        g_minus_p += 1
        if s[i] == "p":
            score -= 1
print(score)
