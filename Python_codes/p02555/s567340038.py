MOD = 1000000007


S = int(input())
Ans = 0

for i in range(1,S//3 +1):
    #iは数列の長さ
    #自由に割り振れるのはremain個
    remain = S - 3*i
    
    #長さiの数列で条件を満たすのはcomb(M+i-1,M)個
    num = 1
    for j in range(1,i):
        num = num*(remain+i-j)
        num = num//j
    num = num%MOD
    Ans = (Ans+num)%MOD

print(Ans)