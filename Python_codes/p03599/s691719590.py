A, B, C, D, E, F = map(int, input().split())
con = -1
ans0 = -1
ans1 = -1
 
for a in range(31):
    for b in range(31):
        if a==0 and b==0:
            continue
        
        for c in range(3001):
            for d in range(3001):
                water = 100*A*a+100*B*b
                sugar = C*c+D*d
                
                if water+sugar>F:
                    break
                
                if sugar>(A*a+B*b)*E:
                    break
                
                if 100*sugar/(water+sugar)>con:
                    con = 100*sugar/(water+sugar)
                    ans0 = water+sugar
                    ans1 = sugar
 
print(ans0, ans1)
