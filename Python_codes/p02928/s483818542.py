n,k = map(int,input().split())
a = list(map(int,input().split()))
cnt1 = 0
for i in range(n):
    for j in range(n-1,i,-1):
        if a[j] < a[j-1]:
            a[j],a[j-1] = a[j-1],a[j]
            cnt1 += 1
cnt1 *= k

cnt2 = 0
for i in range(n):
    for j in range(n):
        if i != j:
            if a[i] > a[j]:
                cnt2 += 1
cnt2 = cnt2*(k*(k-1)//2)

print((cnt1+cnt2)%(10**9+7))