from collections import defaultdict

H, W = map(int, input().split())
a = [list(input()) for _ in range(H)]

def solve() :
    d = defaultdict(int)
    for y in range(H) :
        for x in range(W) :
            d[a[y][x]] += 1
            
    one = 1 if H % 2 == W % 2 == 1 else 0
    two = 0

    if H % 2 == 1 : two += W // 2
    if W % 2 == 1 : two += H // 2
        
    for v in d.values() :
        if v % 4 == 3 :
            one -= 1
            two -= 1
        elif v % 4 == 2 :
            two -= 1
        elif v % 4 == 1 :
            one -= 1
        
        if one < 0 or two < 0 :
            return 'No'
            
    return 'Yes'
    
print(solve())