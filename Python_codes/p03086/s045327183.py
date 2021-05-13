max_len = 0
tmp = 0

S = input()
acgt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in range(len(S)):
    if S[i] in acgt:
        tmp += 1
    else:
        max_len = max(max_len, tmp)
        tmp = 0

max_len = max(max_len, tmp)
print(max_len)
