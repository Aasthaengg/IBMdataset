a, b, k = map(int, input().split())
ans = [1]
n = min(a, b)
for i in range(2, n+1):
    if a%i == 0 and b%i == 0:
        ans += [i]
print(ans[-k])
