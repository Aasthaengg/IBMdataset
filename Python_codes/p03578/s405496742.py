from collections import Counter

n = int(input())
d = Counter(list(map(int, input().split())))
m = int(input())
t = Counter(list(map(int, input().split())))

ans = 'YES'
for key, value in t.items():
    if value > d[key]:
        ans = 'NO'
        break
    else:
        pass
print(ans)