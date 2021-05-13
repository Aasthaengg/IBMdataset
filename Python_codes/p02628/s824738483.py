def mix_juice():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    res = 0
    for i in range(K):
        res += p.pop(0)
    print(res)
    
mix_juice()