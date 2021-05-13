from collections import Counter

def solve():
    H, W = map(int, input().split())
    cnt = Counter()
    for _ in range(H):
        cnt.update(input())
    
    x = []
    for v in cnt.values():
        n = v%4
        if n:
            x.append(n)
    
    yes = "Yes"
    no = "No"

    c = (H&1)+(W&1)

    if c == 0:
        if x:
            return no
        return yes
    
    elif c == 1:
        if H&1:
            a = W
        else:
            a = H
        if sum(x) > a:
            return no
        for y in x:
            if y&1:
                return no
        return yes

    else:
        if sum(x) > H+W-1:
            return no
        o = 0
        for y in x:
            if y&1:
                o += 1
        
        if o == 1:
            return yes
        
        return no

print(solve())