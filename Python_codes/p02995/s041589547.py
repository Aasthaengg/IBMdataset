import math

A,B,C,D = map(int,input().split())

#C,Dの最小公倍数
E = C*D//math.gcd(C,D)
def num_mult(fro,to,mult):
    goal = to//mult
    if fro % mult == 0:
        start = fro // mult
    else:
        start = fro // mult + 1
    
    return goal - start + 1

ans = B-A+1
#Cの倍数
ans -= num_mult(A,B,C)
#Dの倍数
ans -= num_mult(A,B,D)
#C,Dの公倍数
ans += num_mult(A,B,E)

print(ans)