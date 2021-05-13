n,k = map(int, input().split())
s = input()

now = "1"
p = 0
l = []

for i in range(n):
    if s[i] == now:
        p += 1
    else:
        l.append(p)
        if now == "1":
            now = "0"
        else:
            now = "1"
        p = 1

l.append(p)

if s[n - 1] == "0":
    l.append(0)

m = len(l) // 2

ans = 1

if m <= k:
    ans = n
else:
    ans = sum(l[:2 * k + 1])
    nowans = ans
    for i in range(m - k):
        nowans += l[2*(k+i)+1] + l[2*(k+i+1)]
        nowans -= l[2*i] + l[2*i+1]
        ans = max(ans, nowans)

print(ans)