S = input()[::-1]
T = input()[::-1]
ns, nt = len(S), len(T)
ans = None
for i in range(ns-nt+1):
    _S = S[i:i+nt]
    f = True
    for s,t in zip(_S,T):
        if not (s=='?' or s==t):
            f = False
            break
    if f:
        ans = S[:i].replace('?', 'a')+T+S[i+nt:].replace('?', 'a')
        break
print("UNRESTORABLE" if not ans else ans[::-1])