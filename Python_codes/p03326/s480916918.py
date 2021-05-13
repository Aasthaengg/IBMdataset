n,m = map(int,input().split())
bit = [bin(i)[2:].zfill(3) for i in range(2**3)]
ans = -int(1e10)
cake = []
for i in range(n):
    a,b,c = map(int,input().split())
    cake.append((a,b,c))
for i in range(2**3):
    u = []
    cond = bit[i]
    for j in range(n):
        cnt = 0
        for k in range(3):
            if cond[k] == "0":
                cnt += cake[j][k]
            else:
                cnt -= cake[j][k]
        u.append(cnt)
    u.sort(reverse=True)
    ans = max(ans, sum(u[:m]))
print(ans)


