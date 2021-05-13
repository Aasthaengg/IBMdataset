S = input()

alphabet = set(chr(ord('a')+x) for x in range(26))

def F_short(S):
    se = alphabet -set(S)
    x = min(se)
    return S + x
    
def F_long(S):
    if S == ''.join(sorted(alphabet, reverse=True)):
        return '-1'
        
    cand = []
    S = list(S)
    while True:
        x = S[-1]
        if not cand or (x > max(cand)):
            cand.append(S.pop())
            continue
        y = min(ch for ch in cand if ch > x)
        return ''.join(S[:-1]) + y
        
L = len(S)
answer = F_short(S) if L < 26 else F_long(S)
print(answer)