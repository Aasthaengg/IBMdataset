R, G, B, N = map(int, input().split())
li = sorted([R,G,B])
ans = 0
for i in range(N//li[2]+1):
    for j in range((N-R*i)//li[1]+1):
        t = N - li[2]*i - li[1]*j
        if t < 0:
            continue
        if t % li[0] == 0:
            ans+=1
print(ans)