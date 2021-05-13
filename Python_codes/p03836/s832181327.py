sx, sy, tx, ty = map(int, input().split())

ans = []

if tx > sx:
    ans.append('R'*(tx-sx))     #0
    ans.append('L'*(tx-sx))     #2
    ans.append('R'*(tx-sx+1))   #5
    ans.append('L')             #7
    ans.append('L'*(tx-sx+1))   #9
    ans.append('R')             #11
else:
    ans.append('L'*(sx-tx))     #0
    ans.append('R'*(sx-tx))     #2
    ans.append('L'*(sx-tx+1))   #5
    ans.append('R')             #7
    ans.append('R'*(sx-tx+1))   #9
    ans.append('L')             #11

if ty > sy:
    ans.insert(1,'U'*(ty-sy))   #1
    ans.insert(3,'D'*(ty-sy))   #3
    ans.insert(4,'D')           #4
    ans.insert(6,'U'*(ty-sy+1)) #6
    ans.insert(8,'U')           #8
    ans.insert(10,'D'*(ty-sy+1))#10
else:
    ans.insert(1,'D'*(sy-ty))   #1
    ans.insert(3,'U'*(sy-ty))   #3
    ans.insert(4,'U')           #4
    ans.insert(6,'D'*(sy-ty+1)) #6
    ans.insert(8,'D')           #8
    ans.insert(10,'U'*(sy-ty+1))#10

ANS = ''.join(ans)
print(ANS)