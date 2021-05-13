import itertools
 
n, k = map(int, input().split())
p = list(map(int, input().split()))
acc = [0] + list(itertools.accumulate([(x+1)/2 for x in p])) # 累積和を計算
 
ans = max(acc[i]-acc[i-k] for i in range(k, n+1)) # k番目からn番目まで計算
print(ans)
