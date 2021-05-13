N,M = map(int,input().split())
ks = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int,input().split()))
ans=0
for i in range(2**N):
    b="0"*(N-len(bin(i)[2:]))+bin(i)[2:]
    #print(b)
    on=0
    for j in range(M):#各電球ごと　#電球1はスイッチ1,2,5のうち奇数個ついていればよい
        c=0#その電球に必要なスイッチの数用のカウント
        for k in range(N):
            if k+1 in ks[j][1:]:#例えばスイッチ1が電球1に必要なスイッチのリストふ含まれているとき
                if b[k]=="1":
                    c+=1
        if c%2==p[j]:
            on+=1
    if on==M:
        ans+=1
print(ans)