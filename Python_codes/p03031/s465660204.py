n , m = map(int, input().split())
KS = [list(map(int, input().split())) for _ in range(m)]
P = list(map(int, input().split()))

ans = 0
for i in range(2 ** n):
    i_str = bin(i)[2:].zfill(n)
    onNum = 0
    for num, ks in enumerate(KS):
        k = ks[0]
        s = ks[1:]
        p = P[num]
        on = 0
        for sw in s:
            if i_str[sw - 1] == "1":
                on += 1
        if on % 2 == p:
            onNum += 1
    if onNum == m:
        ans += 1

print(ans)


        
        
