N, K = map(int, input().split())
x = list(map(int, input().split()))

ans = []
for i in range(N-K+1):
    l = x[i]
    r = x[i+K-1]
    ans.append(min(abs(l)+abs(l-r), abs(r)+abs(l-r)))

print(min(ans))