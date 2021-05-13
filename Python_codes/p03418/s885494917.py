N,K = map(int, input().split())

if K == 0:
    print(N*N)
    exit()


ans = 0
for b in range(K+1,N+1):
    # N = b * num + rest
    num = N // b 
    rest = N - (b*num)
    # b一周期の中に、余りがK以上になる数字が(b-K)個、残りの中でさらに余りがKを超える物があればそれも加算
    ans += (b - K) * num + max(0, rest-K+1) 


print(ans)