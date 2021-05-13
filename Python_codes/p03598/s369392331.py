N = int(input())
K = int(input())
X = map(int, input().split())
ans = 0
for x in X:
    ans += 2*min(abs(x-K), x)
print(ans)