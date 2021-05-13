n,k = map(int,input().split())
v = [0]+[int(i) for i in input().split()]+[0]
ans = 0
cnt1 = 0
m1 = []
for i in range(n+1):
    cnt1 += v[i]
    if v[i] < 0: m1.append(v[i])
    cnt2 = cnt1
    m2 = m1[:]
    for j in range(n-i+1):
        if i + j > k: break
        r = k - i - j
        cnt2 += v[n+1-j]
        if v[n+1-j] < 0: m2.append(v[n+1-j])
        m2.sort()
        s = cnt2
        s -= sum(m2[:r])
        ans = max(s,ans)
print(ans)