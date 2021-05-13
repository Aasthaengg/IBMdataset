n, k = map(int, input().split())
a = [int(_) for _ in input().split()]
MOD = 10**9+7

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i] > a[j]:
            cnt += 1
ans = cnt * k

dic = dict()
for i in range(n):
    if a[i] in dic:
        dic[a[i]] += 1
    else:
        dic.setdefault(a[i], 1)
dic = sorted(dic.items())
cnt = 0
s = dic[0][1]
for i in range(1, len(dic)):
    cnt += s * dic[i][1]
    s += dic[i][1]
rep = k * (k-1) // 2
ans = (ans + cnt * rep) % MOD
print(ans)