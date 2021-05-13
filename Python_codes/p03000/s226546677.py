n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 1
p = 0

for i in range(n):
    p += a[i]
    if p<x:
        ans+=1
    elif p==x:
        ans+=1
        break
    else:
        break

print(ans)