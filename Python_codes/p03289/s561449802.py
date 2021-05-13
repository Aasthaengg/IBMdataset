S = input()

ans = "AC"

if S[0] != "A":
    ans = "WA"

if S.count("C") != 1:
    ans = "WA"

if not ("C" in S[2:-1]):
    ans = "WA"

for i in range(len(S)):
    if S[i].isupper():
        if S[i] == "A" or S[i] == "C":
            pass
        else:
            ans = "WA"

print(ans)
