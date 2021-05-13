n = int(input())
p = list(map(int, input().split()))

ans = 0

for i in range(n-2):
    a = []
    a.extend([p[i], p[i+1], p[i+2]])
    s = set(a)
    if len(s)==3:
        a3 = sorted(a)
        if a3[1]==a[1]:
            ans += 1
    elif len(s)==2:
        if a[1]<a[2] and a[1]<a[0]:
            ans += 1

print(ans)