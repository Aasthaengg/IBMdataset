n,m = map(int,input().split())
light = [list(map(int,input().split()))[1:] for _ in range(m)]
check = list(map(int,input().split()))
ans = 0
for i in range(2**n):
    for j in range(m):
        cnt = 0
        ok = 1
        for k in light[j]:
            if i >> (k-1) & 1 == 1:cnt += 1
        if cnt%2 == check[j]:
            continue
        else:
            ok=0
            break
    ans += ok 
print(ans)