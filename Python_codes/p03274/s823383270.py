[N,K] = list(map(int,input().split()))
x = list(map(int,input().split()))

#連続する蝋燭を全探索
l=0
r=K-1

ans=2*(10**9)+1
for i in range(N-K+1):
    # print('x[l], x[r]:', x[l], x[r])
    ans = min(ans, min(abs(x[l]), abs(x[r])) + x[r]-x[l])
    l+=1
    r+=1

print(ans)
