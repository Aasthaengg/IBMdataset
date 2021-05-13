def solve():
    S = input()
    T = input()
    
    l = []
    flag = False
    for i in range(len(S)-len(T)+1):
        for s, t in zip(S[i:i+len(T)], T):
            if s != '?' and s != t:
                flag = True
                break
        if flag:
            flag = False
            continue
        
        l.append(S[:i].replace('?', 'a')+T+S[i+len(T):].replace('?', 'a'))
    
    if len(l) == 0:
        return 'UNRESTORABLE'
    else:
        l.sort()
        return l[0]

print(solve())