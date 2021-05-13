N = int(input())
x2 = input()
x10 = int(x2, 2)
popc =  x2.count("1")
#print("x10", x10)
#print("popc", popc)
#popc: Nを2進数で表したときの1の個数

#以下で1つフリップさせた時の入力に対する余りを事前に計算
if popc <= 1:
    xp = x10%(popc+1)
    xm = 0
else:
    xp = x10%(popc+1)
    xm = x10%(popc-1)
#print("xp", xp)
#print("xm", xm)

#以下でフリップさせた場所のみを計算
for i in range(N):
    if x2[i] == "1":
        if popc == 1:
            print(0)
            continue
        tmp = (xm - pow(2, N-i-1, popc-1))%(popc-1)
    else:
        tmp = (xp + pow(2, N-i-1, popc+1))%(popc+1)
        
    #print("tmp", tmp)
    ans = 1
    while tmp > 0:
        tmp %= bin(tmp).count("1")
        ans += 1
    print(ans)
