import math 
MOD = int(1e9)

s = int(input())
if s==1000000000000000000:
    ans = [0,0,MOD,0,0,MOD]
    print(*ans)
    exit()

ans = [0,0,MOD,1]
x,y = 0,0
y = s//MOD + 1
x = MOD - s%MOD
ans.append(x)
ans.append(y)
print(*ans)
