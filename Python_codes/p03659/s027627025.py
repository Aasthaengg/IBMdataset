N = int(input())
a = list(map(int, input().split()))
arai = sum(a)
sunu = 0
ans = 10**20
for i in range(N-1):
    arai -= a[i]
    sunu += a[i]
    ans = min(ans, abs(arai-sunu))
print(ans)
