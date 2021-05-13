from collections import Counter

n = int(input())
d = Counter(list(map(int, input().split())))
ans = -1

for k in sorted(d.keys())[::-1]:
    if ans == -1 and d[k] >= 4:
        print(k*k)
        exit()
    elif ans == -1 and d[k] >= 2:
        ans = k
    elif ans != -1 and d[k] >= 2:
        print(ans*k)
        exit()

print(0)