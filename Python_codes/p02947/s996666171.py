from collections import Counter
N = int(input())
slist = []
for _ in range(N):
    s = sorted(input())
    s = ''.join(s)
    slist.append(s)
slist = Counter(slist)
ans = 0
for i in slist.values():
    if i == 1:
        continue
    ans += (i*(i-1)+2)//2-1

print(ans)
