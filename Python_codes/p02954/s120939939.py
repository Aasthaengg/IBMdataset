S = input()
S = S + "s"
s = [0] * len(S)

rl = "R"
stock = 0
lidx = 0
for i in range(len(S)):
    #print(S[i])
    if S[i] == rl:
        stock += 1
    else:
        if rl == "R":
            s[i-1] += stock // 2 + stock % 2
            s[i] += stock // 2
            lidx = i
        elif rl == "L":
            s[lidx] += stock // 2 + stock % 2
            s[lidx-1] += stock // 2
        rl = S[i]
        stock = 1

    #print(s)

print(" ".join(map(str, s))[:-1])
