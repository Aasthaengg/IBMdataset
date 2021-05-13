A, B, C, D = map(int,input().split())
tx = C - A
ty = D - B

def Ans(U,D,R,L,tx,ty):#U,R,D,L
    tx = abs(tx)
    ty = abs(ty)
    ans = U*ty+R*tx+D*ty+L*tx #1巡目
    ans += L+U*(ty+1)+R*(tx+1)+D+R+D*(ty+1)+L*(tx+1)+U
    return ans

if tx >= 0 and ty >= 0:
    print(Ans("U","D","R","L",tx,ty))
elif tx < 0 and ty < 0:
    print(Ans("D","U","L","R",tx,ty))
elif tx >= 0 and ty <0:
    print(Ans("D","U","R","L",tx,ty))
else:
    print(Ans("U","D","L","R",tx,ty))