s = input()
G  = []
for i in range(len(s)):
    if i % 2 == 0:
        G.append(s[i])
StrG = "".join(G)
print(StrG)
