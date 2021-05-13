N, X = map(int, input().split())
m = []
for _ in range(N):
    mi = int(input())
    m.append(mi)
m.sort()
ans = N
X -= sum(m)
ans += X // min(m)
print(ans)
