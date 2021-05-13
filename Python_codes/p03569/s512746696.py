s = input()
t = s.replace('x', '')

if t != t[::-1] :
    print(-1)
    
else :
    sp = []
    cnt = 0
    for i in s :
        if i != 'x' :
            sp.append(cnt)
            cnt = 0
        else :
            cnt += 1
    
    sp.append(cnt)
    
    ret = 0
    n = len(sp)
    for i in range(n // 2) :
        ret += abs(sp[i] - sp[n-1-i])
        
    print(ret)