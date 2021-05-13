N, K = map(int, input().split())
V = list(map(int, input().split()))
 
ans = 0
for a_plus_b in range(min(N, K) + 1): # a, bの全組み合わせで実施
    for a in range(a_plus_b + 1):
        b = a_plus_b - a
        gems = V[:a] # 左からa番目までを取得
        if b > 0:
            gems += V[-b:] # 右からb番目までを取得
        gems.sort()
        negative_gems = [g for g in gems if g < 0]
        ans = max(ans, sum(gems) - sum(negative_gems[:K - a_plus_b])) # K-(a+b)までネガティブのものを捨てられる 
print(ans)