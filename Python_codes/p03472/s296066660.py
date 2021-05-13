n, k = map(int, input().split())
attacks = []
mxa = 0

for i in range(n):
    a, b = map(int, input().split())
    attacks.append([a, b])
    mxa = max(mxa, a)
attacks = sorted(attacks, key=lambda x: -x[1])

ans = 0
idx = 0
while k > 0:
    if idx < n and attacks[idx][1] > mxa:
        k -= attacks[idx][1]
        idx+=1
    else:
        ans += (k)//mxa
        if k%mxa != 0:
            ans += 1
        break
    ans+=1
print(ans)

