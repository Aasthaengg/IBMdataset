n = int(input())
a = list(map(int,input().split()))
ad = {}
for i in range(n):
    if a[i] in ad:
        ad[a[i]] +=1
    else:
        ad[a[i]] = 1
ans = 0
for j in ad.values():
    ans += j*(j-1)//2

for i in range(n):
    j = ad[a[i]]
    print(ans-j*(j-1)//2+(j-1)*(j-2)//2)