n = int(input())
a=[int(input()) for i in range(n)]

ans=0
last=0
for i in range(n):
    if (i < a[i]) or (last + 1 < a[i]):
        print(-1)
        exit()
    elif last+1==a[i]:
        last=a[i]
    else: # last >= a[i]
        ans+=last
        last=a[i]

ans+=last
print(ans)