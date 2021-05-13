N = int(input())
a = list(map(int,input().split()))
l = [set([]) for k in range(N+1)]
ans = 0
for k in range(N):
    if k+1 in l[a[k]]:
        ans += 1
    l[k+1].add(a[k])
print(ans)
