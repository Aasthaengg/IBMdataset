n = int(input())
aa = list(map(int, input().split()))
bit = [[0] * 21 for _ in range(n)]
for i, a in enumerate(aa):
    for j in range(21):
        a, m = divmod(a, 2)
        if m: bit[i][j] = 1
#for x in bit:
#    print(x)
last = [-1] * 21
L = R = 0
ans = 0
while R < n:
    out = []
    nextL = []
    for j in range(21):
        if bit[R][j]:
            if last[j] == -1:
                last[j] = R
            else:
                out.append(j)
                nextL.append(last[j])
                last[j] = R
    #    print(L,R,ans,last)
    if out:
        #        print(out)
        d1 = R - L
        L = max(nextL) + 1
        d2 = R - L + 1
        #        print(d1,d2,(d1+d2)*(d1-d2+1)//2)
        ans += (d1 + d2) * (d1 - d2 + 1) // 2
        for j in range(21):
            if last[j] < L:
                last[j] = -1
    R += 1
d = n - L
ans += d * (d + 1) // 2
print(ans)
