n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt1 = 0
cnt2 = 0
seen = []
for i in a:
    for j in seen:
        if i<j:
            cnt1 += 1
    seen.append(i)
for i in a:
    for j in seen:
        if i<j:
            cnt2 += 1
ans = cnt1*k+cnt2*k*(k-1)//2
print(ans%(10**9+7))