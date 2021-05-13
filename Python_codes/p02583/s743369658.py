n = int(input())
l = list(map(int,input().split()))
ans = 0
for a in range(n-2):
    for b in range(a,n-1):
        for c in range(b,n):
            if l[a]+l[b] > l[c] and l[b]+l[c] > l[a] and l[c]+l[a] > l[b]:
                if l[a] != l[b] and l[b] != l[c] and l[a] != l[c]:
                    ans += 1
print(ans)