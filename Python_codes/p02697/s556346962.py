N, M = map(int,input().split())

# M個の対戦場は、それぞれ違う距離の対戦相手と対戦するようにする
# そのために、1~Nのうち前半を奇数差、後半を偶数差で構成する
a = 1
if M%2 == 1:
    # M~1までの奇数を順に
    for i in range(M,0,-2):
        print(str(a) + ' ' + str(a+i))
        a+=1
    a = N
    # M-1~2までの偶数を順に
    for i in range(M-1, 1, -2):
        print(str(a) + ' ' + str(a - i))
        a-=1
elif M%2 == 0:
    # M-1~1までの奇数を順に
    for i in range(M-1,0,-2):
        print(str(a) + ' ' + str(a+i))
        a+=1
    a = N
    # M~2までの偶数を順に
    for i in range(M, 1, -2):
        print(str(a) + ' ' + str(a - i))
        a-=1
