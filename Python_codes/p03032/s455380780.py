import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0

for l in range(min(N, K) + 1): #左側から取る個数
    left = N - l #筒に残っている数
    for r in range(min(left, K - l) + 1): #右側から取る個数
        k = K - l - r #捨てる個数
        tmp = V[:l] + V[N - r:]
        tmp.sort(reverse = False)
        t = sum(tmp)
        for i in range(min(k, l + r)): #最大捨てることができる個数
            if tmp[i] < 0:
                t -= tmp[i]
            else:
                break
        
        ans = max(ans, t)

print (ans)