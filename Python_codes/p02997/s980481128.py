N, K = map(int,input().split())
if K>((N-1)*(N-2))//2:
    print(-1)
else:
    ans = []
    for i in range(N-1):
        ans.append([1,i+2])
    if N!=2:
        k = 2
        l = 2
        for i in range(((N-1)*(N-2))//2-K):
            if l==N:
                k+=1
                l=k+1
            else:
                l+=1
            ans.append([k,l])
    print(len(ans))
    for i in ans:
        print(*i)