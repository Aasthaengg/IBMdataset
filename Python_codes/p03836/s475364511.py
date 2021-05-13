sx,sy,tx,ty= map(int,input().split())
ans = ''
if sx > tx:
    R = 'L'
    L = 'R'
else:
    R = 'R'
    L = 'L'
if sy > ty:
    U = 'D'
    D = 'U'
else:
    U = 'U'
    D = 'D'
if sx == tx:
    ans += U * (abs(ty-sy))
    ans += L
    ans += D * (abs(ty-sy))
    ans += R * 2
    ans += U * (abs(ty-sy))
    ans += L
    ans += U
    ans += R * 2
    ans += D * (abs(ty-sy)+2)
    ans += L * 2
    ans += U
elif sy == ty:
    ans += R * (abs(tx-sx))
    ans += U
    ans += L * (abs(tx-sx))
    ans += D * 2
    ans += R * (abs(tx-sx))
    ans += U
    ans += R
    ans += D * 2
    ans += L * (abs(tx-sx)+2)
    ans += U * 2
    ans += R
else:
    ans += U * (abs(ty-sy))
    ans += R * (abs(tx-sx))
    ans += U
    ans += L * (abs(tx-sx)+1)
    ans += D * (abs(ty-sy)+1)
    ans += R * (abs(tx-sx)+1)
    ans += U * (abs(ty-sy))
    ans += R
    ans += D * (abs(ty-sy)+1)
    ans += L * (abs(tx-sx)+1)
    ans += U
print(ans)