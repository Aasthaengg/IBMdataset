n = int(input())
a = list(map(int,input().split()))
ruiseki_WA=[0]
for i in range(n):
    ruiseki_WA.append(ruiseki_WA[i]+a[i])
ans=float("inf")
for i in range(n):
    kari=abs(ruiseki_WA[i]-(ruiseki_WA[-1]-ruiseki_WA[i]))
    ans=min(ans,kari)
print(ans)