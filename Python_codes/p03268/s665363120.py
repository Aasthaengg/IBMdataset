N, K = map(int, input().split())

if K % 2 == 1: #Kが奇数
    count = N // K
    print (count ** 3)
else:
    count = N // K #Kの倍数の個数
    ans = count ** 3
    count = N // (K // 2) - N // K
    ans += count ** 3
    print (ans)