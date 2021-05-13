N, K = list(map(int, input().split()))
td = sorted([list(map(int, input().split())) for _ in range(N)],key=lambda x:-x[1])
q = []
ans = 0
s = set()
for i in range(K):
    ans += td[i][1]
    if td[i][0] in s:
        q.append(td[i][1])
    s.add(td[i][0])
ans += len(s)**2
k1 = K
ans1 = ans
while k1 < N and q:
    if td[k1][0] not in s:
        ans1 += td[k1][1] - q.pop() - len(s)**2 + (len(s)+1)**2
        ans = max(ans,ans1)
        s.add(td[k1][0])
    k1 += 1
print(ans)