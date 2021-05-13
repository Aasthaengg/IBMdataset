N,K = map(int,input().split())
P = list(map(int,input().split()))
for i in range(N):
    P[i] -= 1
C = list(map(int,input().split()))
ans = max(C)
for i in range(N):
    p = i
    d = []
    while True:
        p = P[p]
        d.append(C[p])
        if p == i:
            break
    #print(d,sum(d))
    val = 0
    for j in range(min(K,len(d))):
        val += d[j]
        ans = max(ans,val)
        #print(val,i,j)



    if K > len(d):
        k = K % len(d)
        val = (K//len(d)) * sum(d)
        ans = max(ans,val)
        for j in range(k):
            val += d[j]
            ans = max(ans,val)

        val = (K//len(d)-1) * sum(d)
        for j in range(len(d)):
            val += d[j]
            ans = max(ans,val)

print(ans)
