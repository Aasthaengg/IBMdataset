N,M=map(int,input().split())
ab = [tuple(map(int,input().split())) for _ in range(M)]
ab.sort(key=lambda x: x[1])
ans = 0
s = 0 #最新の切断点
for i in range(M):
    a, b = ab[i]
    if a >= s: # aを今の最新の切断点で対処できないなら、
        #そのaに対するb(これは必ず対処できる)で切る
        s = b
        ans += 1
print(ans)
