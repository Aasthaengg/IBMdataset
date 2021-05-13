N = int(input())
S = [input() for _ in range(N)]
B_A = 0
notB_A = 0
B_notA = 0
ans = 0
for s in S:
    if s[0] == "B" and s[-1] == "A":
        B_A += 1
    elif s[0] == "B":
        B_notA += 1
    elif s[-1] == "A":
        notB_A += 1
    for i in range(len(s) - 1):
        if s[i : i + 2] == "AB":
            ans += 1

if B_A:
    ans += B_A - 1
    if notB_A > 0:
        ans += 1
        notB_A -= 1
    if B_notA > 0:
        ans += 1
        B_notA -= 1

print(ans + min(notB_A, B_notA))
