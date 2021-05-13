S = input()
T = input()
n = len(S)
chars1 = []
chars2 = []
pos1 = {}
pos2 = {}
for i in range(n):
    c1 = S[i]
    c2 = T[i]
    if c1 in pos1:
        chars1[pos1[c1]].append(i)
    else:
        pos1[c1] = len(chars1)
        chars1.append([i])

    if c2 in pos2:
        chars2[pos2[c2]].append(i)
    else:
        pos2[c2] = len(chars2)
        chars2.append([i])
print('Yes' if chars1 == chars2 else 'No')