D, G = map(int, input().split())
pi = []
ci = []
for _ in range(D):
    p, c = map(int, input().split())
    pi.append(p)
    ci.append(c)

ans =  float('inf')


for bit in range(1 << D ):
    sum = 0
    count = 0
    nokori = set(range(1, D + 1))

    for i in range(D):
        # if bit & (1 << D)で、bitにiが含まれているか（フラグが立っているか）を判定してくれるらしい
        #今回は、i×100点の問題を全て解く場合の処理を書く
        if bit & (1 << i):
            sum +=  100 * (i + 1) * pi[i] + ci[i]
            count += pi[i]
            nokori.discard(i + 1)

    if (sum < G ):
        use = max(nokori)
        n = min(pi[use-1], (G- sum )// (use * 100) )
        if n < 1:
            n = 1
        count += n
        sum   += n * 100 * use 

    if  (sum >= G):
        ans = min(count, ans)

print(ans)

