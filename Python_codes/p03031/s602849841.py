N,M=map(int,input().split())
s = []
for _ in range(M):
    s.append(list(map(lambda x:int(x)-1,input().split()))[1:])
p = list(map(int,input().split()))
ans = 0
for i in range(2**N):
    fl = True
    for j in range(M):
        cnt = 0
        for sw in s[j]:
            if (i >> sw) & 1:
                cnt += 1
        if cnt % 2 != p[j]:
            fl = False
            break
    if fl:
        ans += 1
print(ans)