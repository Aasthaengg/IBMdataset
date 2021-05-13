n,h = map(int,input().split())
katana_a = []
katana_b = []
for i in range(n):
    a,b = map(int,input().split())
    katana_a.append(a)
    katana_b.append(b)
amax = max(katana_a)
katana_b.sort(reverse=True)
ans = 0
k = 0
while h > 0:
    if k == n:
        break
    if katana_b[k] > amax:
        h -= katana_b[k]
        ans += 1
        k += 1
    else:
        break
if h <= 0:
    print(ans)
else:
    print(ans + (h+amax-1)//amax)




