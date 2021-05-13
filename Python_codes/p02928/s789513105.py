n,k = map(int, input().split())
a = list(map(int, input().split()))
MOD = 10 ** 9 + 7

cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if a[i] > a[j]: cnt += 1
y = 0
for a1 in a:
    for a2 in a:
        if a1 > a2: y += 1

ans = (cnt*k + y*k*(k-1)//2)%MOD
print(ans)