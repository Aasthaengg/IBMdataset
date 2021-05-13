N, K = map(int, input().split())
H = list(map(int, input().split()))

I = sorted(H,reverse=True)

if len(H) <= K:
    print(0)
elif K == 0:
    print(sum(H))
else:
    for i in range(K):
        I[i] = 0
    print(sum(I))
