n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

from collections import Counter
dc = Counter(d)
tc = Counter(t)

ans = 'YES'
for dif, num in tc.items():
    if dc[dif] < num:
        # 足りない
        ans = 'NO'
        break

print(ans)