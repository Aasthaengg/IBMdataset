n = int(input())
a = []
xy = [list() for _ in range(n)]

for i in range(n):
    a += [int(input())]
    for j in range(a[i]):
        xy[i] += [list(map(int,input().split()))]


honestnum = []

for i in range(2**n):
    flag = True
    #(if bin(i).count("1") == _:)
    #print("次のiいくよー"+"i:"+str(i)+",2進法で"+str(bin(i))[2:])
    for j in range(n):
        if (i>>j)&1 == 1:
            #print("下から"+str(j+1)+"桁目は1,つまり,index"+str(j)+"が1だね")
            for k in range(a[j]):
                if xy[j][k][1] != (i>>(xy[j][k][0]-1)&1):
                    flag = False
                    break
        
    if flag:
        #print("わーい")
        honestnum += [bin(i).count("1")]
print(max(honestnum))
