def check_val(ind):
    if ind > len(b): return False 
    if b[ind-1] == ind:
        ans.append(ind)
        del b[ind-1]
        if ind not in b: set_b.remove(ind)
        return True
    else:
        return False


N,*b = map(int,open(0).read().split())
if b[0] != 1: 
    print(-1)
    exit()

set_b = sorted(set(b),reverse=True)
ans = []

while len(b) != 0:
    flg = False
    for i in set_b:
        flg = check_val(i)
        if flg: break
    
    if flg == False:
        print(-1)
        exit() 
else: #消せるものがなくなった
    print(*ans[::-1],sep="\n")
    
        
    
