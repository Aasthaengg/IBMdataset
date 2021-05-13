from collections import defaultdict
n,k = map(int,input().split())
s = [0] + list(map(int,input().split()))
for i in range(n):
    s[i+1] += s[i]
dic = defaultdict(int)
ans = 0
for i in range(n+1):
    x = (s[i]-i) % k
    ans += dic[x]
    dic[x] += 1
    if i >= k-1:
        y = (s[i-k+1]-(i-k+1)) % k
        dic[y] -= 1
print(ans)
