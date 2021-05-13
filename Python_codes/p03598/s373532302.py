N = int(input())
K = int(input())
S = list(map(int, input().split()))
ans = 0
for num in S:
    ans += min(num, K-num)*2
print(ans)