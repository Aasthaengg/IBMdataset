n, m = list(map(int, input().split()))

switch = [[] for _ in range(m)]

for i in range(m):
    ks = list(map(int, input().split()))
    switch[i] = ks[1:]


p = list(map(int, input().split()))

ans = 0
#print(switch)

for i in range(2 ** n):
    flag = [False] * n
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            flag[j] = True

    #print(flag)
    f = True    
    for k in range(m):
        c = 0
        for j in switch[k]:
            if flag[j-1]:
                c += 1
        if c % 2 != p[k]:
            f = False
            break
        
    if f:
            ans += 1

print(ans)

