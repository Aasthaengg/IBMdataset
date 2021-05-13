N,M = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(M)]


ab.sort(key=lambda x: x[1])
ans = 1
pre = ab[0][1]
for ele in ab[1:]:
    if pre > ele[0]:
        continue
    pre = ele[1]
    ans += 1
print(ans)




