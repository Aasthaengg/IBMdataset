N , K = map(int, input().split())
A = list(map(int, input().split()))
s = sum(A)
divisor = []
n = 1
while n ** 2 <= s:
    q, r = divmod(s, n)
    if r == 0:
        divisor.append(q)
        divisor.append(n)
    n += 1
if n ** 2 == s:
    divisor.pop()
ans = 1
for d in divisor:
    m = []
    for a in A:
        m.append(a % d)
    m.sort(reverse=True)
    l = sum(m) // d
    a = l * d - sum(m[:l])
    if a <= K:
        ans = max(ans, d)
print(ans)