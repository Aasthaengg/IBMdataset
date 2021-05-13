D = int(input())
c = list(map(int,input().split()))
m = sum(c)
S = []
d = []
ans = 0
for i in range(D) :
    s = list(map(int,input().split()))
    S.append(s)
for i in range(D) :
    t = int(input())
    d.append(t)
    ans += S[i][t-1]
    for j in range(26) :
        if j+1 not in d :
            ans -= c[j] * (i+1)
        else :
            a = [k for k, x in enumerate(d) if x == j+1 ]
            ans -= c[j] * (i-a[-1])
    print(ans)


    


