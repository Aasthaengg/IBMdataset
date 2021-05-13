n = int(input())
m = list(map(int, input().split()))
ans = m[0] * 2
for i in range(n-2):
    if m[i] > m[i+1]:
        ans += 2 * m[i+1]
        ans -= m[i]
        continue
    ans += max(m[i], m[i+1])
print(ans)