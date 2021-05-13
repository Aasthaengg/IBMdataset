S = input()
W = []
for i in range(len(S)):
    if S[i] == "W":
        W.append(i)

c=0
for i in range(len(W)):
    c+= W[i] - i

print(c)
