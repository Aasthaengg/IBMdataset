S = input()
c = 0
i = 0
ac = 0
while i < len(S):
    if S[i] == "A":
        ac += 1
    elif S[i:i+2] == "BC":
        c += ac
        i += 1
    else:
        ac = 0
    i += 1
print(c)
