N,K = map(int,input().split())
 
#奇数の時
if K%2:
    a = N//K
    print(a**3)
#偶数の時
else:
    #Nまででa,b,cそれぞれがKで割り切れる数(割り切れる数同士の和も割り切れる)
    a = N//K
    #あまりがk/2(和がkの倍数になる場合)
    b = (N+K//2)//K
    print(a**3 + b**3)