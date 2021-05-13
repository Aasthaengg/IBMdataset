N, M = map(int, input().split())
x = 1900 * M + 100*(N-M)
ans = x
p = 1
for i in range(1,10000):
    p *= 1-(0.5)**M
    ans += x * p
print(round(ans))