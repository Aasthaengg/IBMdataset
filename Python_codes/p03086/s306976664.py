import itertools

S = list(input())
Idxs = list(itertools.combinations(range(len(S)), 2)) 

def ACGT(Word):
    for w in Word:
        if w not in ["A", "C", "G", "T"]:
            return 0
    return len(Word)

ans = 0

for s in S:
    if s in ["A", "C", "G", "T"]:
        ans = 1
        break

for idx in Idxs:
    tmp = S[idx[0]:idx[1]+1]
    ans = max(ans, ACGT(tmp))
    
print(ans)