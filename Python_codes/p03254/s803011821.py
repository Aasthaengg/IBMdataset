N,x=map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans=0


if sum(a)<x:
    print(N-1)
else:
    for i in range(len(a)):
        if x>=a[i]:
            x -= a[i]
            ans += 1
        else:
            break
    print(ans)

