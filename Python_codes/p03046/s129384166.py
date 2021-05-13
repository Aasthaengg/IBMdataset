M, K = map(int, input().split())
if K>(1<<M)-1:
    print(-1)
elif M == 1 and K == 1:
    print(-1)
elif M == 1 and K == 0:
    print(0, 0, 1, 1)
elif M == 0 and K == 0:
    print(0, 0)
elif M == 0:
    print(-1)
else:
    N = 1<<M
    ans = list(range(K))+list(range(K+1, N))+[K]+list(range(K+1, N))[::-1]+list(range(K))[::-1]+[K]
    print(*ans)