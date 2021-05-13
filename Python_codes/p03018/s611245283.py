S = input()

NS = ""
i = 0
while i < len(S):
    if S[i] == "A":
        NS += "A"
    elif i + 1 < len(S) and S[i] == "B" and S[i + 1] == "C":
        NS += "X"
        i += 1
    else:
        NS += "Z"
    i += 1

NS = NS[::-1]
res = 0
pos = -1

for i, s in enumerate(NS):
    if pos != -1 and s == "A":
        res += i - pos
        pos += 1
    elif pos == -1 and s == "X":
        pos = i
    elif s == "Z":
        pos = -1

print(res)
