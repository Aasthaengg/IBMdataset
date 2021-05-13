N, K = map(int, input().split())

# 全てのbの候補について、aの候補の個数をかけ合わせる

if K == 0:
    ans = N**2
else:
    ans = 0
    for i in range(1,N-K+1):
        ans += i
        a_start = 2*K+i
        while a_start <= N:
            if a_start+i > N :
                ans += N - a_start +1
            else:
                ans += i
            a_start += K+i
print(ans)