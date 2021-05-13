N, K = map(int, input().split())
if K > (N-1)*(N-2)//2:
    print(-1)
else:
    s = (N-1)*(N-2)//2
    ans = []
    for i in range(2, N+1):
        ans.append([1, i])
    for i in range(2, N):
        if s == K:
            break
        for j in range(i+1, N+1):
            if s == K:
                break
            ans.append([i, j])
            s -= 1
    print(len(ans))
    for i, j in ans:
        print(i, j)