#解説参照
#「下の桁と」mod4「のみで決まる」
# 正負考慮しなくてもこれで
ans = []
n = int(input())
if n==0:
    print(0)
    exit()
while n:
    m = n%4
    if m == 0:
        ans.extend(["0","0"])
    elif m==1:
        ans.extend(["1","0"])
    elif m==2:
        ans.extend(["0","1"])
        n+=4
    else:
        ans.extend(["1","1"])
        n+=4
    n//=4
ans.reverse()
if ans[0]=="1":
    print(''.join(ans))
else:
    print(''.join(ans[1:]))

