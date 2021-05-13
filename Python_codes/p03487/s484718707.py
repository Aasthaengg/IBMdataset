from collections import Counter

N = int(input())

a = list(map(int,input().split()))

a = Counter(a)

ans = 0
for i in a:
    if i <= a[i]:
        ans+=a[i]-i
    else:
        ans+=a[i]

print(ans)