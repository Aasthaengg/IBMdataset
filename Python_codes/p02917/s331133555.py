n,*bb = map(int, open(0).read().split())

ans = bb[0] + bb[-1]

for i in range(n-2):
    ans += min(bb[i],bb[i+1])

print(ans)