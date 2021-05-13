N, M = map(int, input().split())
k_s = [list(map(int, input().split())) for i in range(M)]
p = list(map(int, input().split()))
ans=0
for i in range(2**N):
    for u in range(M):
        t=True
        num=0
        for y in range(1,len(k_s[u])):
            #print(bin(i),u,y-1,bin(i >> (y-1)))
            if ((i >> (k_s[u][y]-1)) & 1):
                num+=1
        if not num%2==p[u]:
            t=False
        if not t :
            break
    else:
        #print(bin(i))
        ans+=1
print(ans) 