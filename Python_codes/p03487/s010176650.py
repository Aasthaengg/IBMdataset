from collections import Counter
n = int(input())
aaa = list(map(int, input().split()))
cnt_a = Counter(aaa)
ans = 0
for key in cnt_a.keys():
    value = cnt_a[key]
    if key > value:
        ans += value
    elif key < value:
        ans += value - key
    else:
        continue
print(ans)