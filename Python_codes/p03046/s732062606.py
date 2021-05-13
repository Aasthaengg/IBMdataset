M,K = map(int,input().split())
if [M,K] == [1,1] or K>=2**M:
    print(-1)
elif [M,K] == [1,0]:
    print('0 0 1 1')
else:
    ans = []
    for i in range(2**M):
        if i != K:
            ans.append(i)
    ans = ans+[K]+ans[::-1]+[K]
    print(*ans)