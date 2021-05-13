ATCG = ['A', 'T', 'C', 'G']
S = input()

counts = []
a = 0
i = 0
while i < len(S):
    if S[i] in ATCG:
        a += 1
    else:
        counts.append(a)
        a = 0
    
    i += 1
    if i == len(S):
        counts.append(a)

print(max(counts))