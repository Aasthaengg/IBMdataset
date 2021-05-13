n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt1 = 0
for i in range(n - 1):
    for  j in range(i + 1, n):
        if a[i] > a[j]:
            cnt1 += 1

a.sort()
cnt2 = 0
c = 0
i = 0
c_n = a[0]
while True:
    cnt = 0
    while a[i + cnt] == c_n:
        cnt +=1
        if i + cnt == n:
            break
    cnt2 += cnt*c
    c += cnt
    i += cnt
    if i == n:
        break
    c_n = a[i]

ans = cnt1*k + cnt2*k*(k - 1)//2
print(ans%(10**9 + 7))