mod = 10**9 + 7


n = int(input())
s1 = input(); s2 = input()

s = ""
i = 0
while i < n:
    if s1[i] == s2[i]:
        s += "A"
        i += 1
    else:
        s += "B"
        i += 2

answer = 3 if s[0] == "A" else 6
for i in range(len(s) - 1):
    if s[i] + s[i + 1] == "AA":
        answer *= 2
    elif s[i] + s[i + 1] == "AB":
        answer *= 2
    elif s[i] + s[i + 1] == "BA":
        answer *= 1
    else:
        answer *= 3
    answer %= mod

print(answer)
