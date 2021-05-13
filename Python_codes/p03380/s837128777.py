n = int(input())
l = list(map(int,input().split()))

if n==2:
    print(max(l),min(l))
    exit()
maxi = max(l)
med = maxi//2
d = 10**9+1
ans = -1

for i in range(n):
    x = l[i]
    if l[i] > med:
        x = maxi-l[i]
    if med-x < d:
        d = med-x
        ans = l[i]

print(maxi,ans)