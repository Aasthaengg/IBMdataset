from bisect import bisect_right

N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
#a,bの累積和
A_sum = [0]
B_sum = [0]
for i in range(N):
    A_sum.append(A_sum[i]+A[i])
for i in range(M):
    B_sum.append(B_sum[i]+B[i])

ans = 0
#Aについて0-N冊読む場合の全探索
for i in range(N+1):
    cntA = i #Aをi冊読む
    rest = K - A_sum[i] #残り時間rest分
    if rest < 0:
        break
    cntB = bisect_right(B_sum,rest)-1 #Bで読むことができる冊数を二分探索で求める
    ans = max(ans,cntA + cntB)
print(ans)