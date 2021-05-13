S = int(input())
# 10**9 * y - x = S
if S <= 10**9:
    print(0,0,S,0,0,1)
else:
    if S != 10**18:
        y = (S + 10**9) // 10**9
        x = abs((10**9) * y - S)
        print(0,0,10**9,1,x,y)
    else:
        print(0,0,10**9,0,0,10**9)