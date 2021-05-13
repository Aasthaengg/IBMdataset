N = int(input())
A = list(map(int,input().split()))
k = sum(A)
###syuutenの個数
c = 1  
###考えている列の〇の個数(次の列につながる個数)
aa = 1
ans = 1
if A[0] != 0:
    aa = 2
    if N != 0:
        print(-1)
    else:
        if A[0] == 1:
            print(1)
        else:
            print(-1)
else:
    for i in range(1,N + 1):
        c *= 2
        ##次の列につながる個数の最大値
        if A[i] > c:
            ###A[i]はここが終点になるということ。終点の方が多いことは認められない
            aa = 0
            break
        elif A[i] == c:
            ###終点と同数だとこれより下には繋がらない。もし最下段でなければアウト
            if i != N:
                aa = 0
                break
            else:
                ans += c
        else:
            c -= A[i]
            k -= A[i]
            ans += A[i]
            ###終点の個数を引く。ここで終点の個数だけansを足す
            if c >= k:
                ###次の列につながる個数はこれよりしたにある終点の個数を超えれない
                c = k
            ans += c
            ###この段で下につながる個数を足す

if aa == 0:
    print(-1)
elif aa == 1:
    print(ans)