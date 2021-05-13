"""
ビット全探索
"""
n, m = map(int, input().split())
lamps = [list(map(lambda x:int(x)-1, input().split()))[1:] for _ in range(m)]
p = list(map(int, input().split()))
ans = 0
#ビット全探索
for i in range(2**n) :
    for r in range(m) :
        on = 0
        for j in range(n) :
            #j桁目が1であるかどうかを調べる
            #jがsに含まれているかどうか調べる
            if (i>>j) & 1 == 1 and j in lamps[r] :
                on += 1
        if on % 2 != p[r] :
            break
    else :
        ans += 1
print(ans)
